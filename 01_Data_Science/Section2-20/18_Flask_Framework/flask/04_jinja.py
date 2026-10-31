from flask import Flask, render_template, request


'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} comments
'''


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if (request.method == 'POST'):
        name = request.form['name']
        return f'Hello {name}'
    
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if (request.method == 'POST'):
        name = request.form['name']
        return f'Hello {name}'
    
    return render_template('form.html')

# Variable Rule

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'Passed'.upper()
    else:
        res = 'Failed'.upper()
    return render_template('result.html', results=res)

# using for
@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score >= 50:
        res = 'Passed'.upper()
    else:
        res = 'Failed'.upper()

    exp = {'score': score, 'res': res}

    return render_template('results.html', results=exp)

# using if
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result_if.html', results=score)


if __name__=="__main__":
    app.run(debug=True)
