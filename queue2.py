
from threading import Thread ,Lock


from functions import worker
from queue import Queue



if __name__ =="__main__":
    lock = Lock()
    q=Queue()
    # q.put(1)
    # q.put(2)
    # q.put(3)
    #
    # first =q.get()
    # print (first )
    # q.task_done()
    # q.join()
    #
    # print("end main")

    num_threads = 10

    for i in range (num_threads):
        thread =Thread(target= worker ,args=(q,lock))
        thread.daemon= True
        thread.start()


    for i in range (1,21):
        q.put(i)

    q.join()










