import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(2)
        print(f"Square number {i**2}", flush=True)

def cube_num():
    for i in range(5):
        time.sleep(2)
        print(f"Cube number {i**3}", flush=True)

if __name__ == '__main__':
    # Create 2 processes
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)

    t = time.time()

    # Start the processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    elapsed_time = time.time() - t
    print(f"Total time taken: {elapsed_time:.2f} seconds")