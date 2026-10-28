'''
Multi processing: for CPU-bound tasks
Factorial calculations, for large numbers, involves significant computational work.
distribute the workload across multiple cpu cores.
'''

from concurrent.futures import ProcessPoolExecutor
import time
from math import factorial

def compute_factorial(number):
    print(f'Computing the factorial of {number}')
    result = factorial(number)
    print(f'The result is {result}')
    return result

numbers = [5000, 7000, 700, 800]

if __name__ == '__main__':

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(compute_factorial, numbers)

    end_time = time.time()

    print(f'Time taken {end_time - start_time} seconds')
    print(f'Results {results}')
