import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"number {i}",flush=True)

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter {letter}",flush=True)

# Creating 2 threads
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)

start_time = time.time()

# Start the threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

elapsed_time = time.time() - start_time
print(f"Total time taken: {elapsed_time:.2f} seconds")