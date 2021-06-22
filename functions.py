import time
from threading import Lock, current_thread
from queue import Queue


q=Queue()


database_value =1

lock = Lock()
def square_numbers():
    for i in range(100):
        i*i


def increase (lock):
    global database_value
    with lock:
        local_copy = database_value
        # processing
        local_copy += 3
        time.sleep(0.1)
        # print(local_copy)
        database_value = local_copy
        # print(database_value)


def worker (p,lock) :

    while True  :
        value= p.get()

        with lock :
            print (f'in {current_thread().name}  Got{value}')
    q.task_done()




