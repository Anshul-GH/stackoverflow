import threading
import time

start = time.perf_counter()


def square(y):
    print('Starting processing')
    for x in range(y):
        i = x * x
    print(f'Done processing {i}')

threads = []

# creating thread
for _ in range(10):
    thread = threading.Thread(target=square, args=[100])
    # starting thread
    thread.start()
    threads.append(thread)

# makes sure that the threads complete before moving to the rest of the code
for i in threads:
    i.join()




finish = time.perf_counter()

print(f'Done processing in {round(finish - start, 4)} second(s).')