# Put and Delete (HTTP Methods)
# Working with API's - JSON 

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to the home page</h1>'

# Initializing global items list

items = [
    {'id': 1, 'name': 'This is item 1', 'description': 'this is description of item 1'},
    {'id': 2, 'name': 'This is item 2', 'description': 'this is description of item 2'}
]

# Get all the items

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get single item

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item Not Found'})
    return jsonify(item)

# Add a new item

@app.route('/items', methods=['POST'])
def add_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'Item Not Found'})
    
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }

    items.append(new_item)
    return jsonify(new_item)

# Update a existing item

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item Not Found'})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete an item

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item Not Found'})

    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': 'Item deleted'})


if __name__ == "__main__":
    app.run(debug=True)

