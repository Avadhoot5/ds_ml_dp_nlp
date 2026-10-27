# Allows you to create processes that runs in parallel
# when to use -> 
# CPU-Bound Tasks that are heavy on CPU usage (mathematical, data computation)
# Parallel execution to use multiple cores of the CPU

import time
from multiprocessing import Process

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square: {i * i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Square: {i * i * i}')

if __name__ == "__main__":

    # create the process
    p1 = Process(target=square_numbers)
    p2 = Process(target=cube_numbers)

    # start the process
    start_time = time.time()
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    end_time = time.time()

    print(f'{(end_time - start_time):5f}')
