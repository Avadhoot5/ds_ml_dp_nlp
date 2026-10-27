# When to use multi threading
# I/O bound tasks: Tasks that spend more time waiting for I/O operations (eg. file operation, n/w requests).
# Concurrent execution: when you want to increase throughput of your app by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number: {i}')

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}')

# create thread

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

start_time = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()

print(f'{(end_time - start_time):5f}')

# print_numbers()        
# print_letters()


