### multithreading with thread pool executer

from concurrent.futures import ThreadPoolExecutor
import time




def print_number(number):
        time.sleep(2)
        return f"Number {number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(print_number,numbers)

for num in result:
    print(num)