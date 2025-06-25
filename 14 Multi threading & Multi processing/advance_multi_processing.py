### multiprocessing using processpoolExecutor


import time
from concurrent.futures import ProcessPoolExecutor


def square(num):
    time.sleep(1)
    return f"squared {num*num}"

number = [1,2,3,4,5,6,7,8,9,10]

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        result = executor.map(square, number)

    for numb in result:
        print(numb)

