'''

Real-world example:- Multiprossesing for CPU-bound task
Scenario: Factorial calculation

'''

import multiprocessing
import math
import sys
import time

##increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

#function to compute factorials of a givinn number

def compute_fact(num):
    print("computing factorial of", num)
    result =  math.factorial(num)
    print("result is", result)
    return result

if __name__ == '__main__':
    numbers =[5000,6000,7000,8000,9000,10000]
    start = time.time()
    #create pool of worker process
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_fact, numbers)

    end = time.time()-start
    print("time is", end)

    print("Results is", results)
    print("time is", end,"seconds")
