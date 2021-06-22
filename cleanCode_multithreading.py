from threading import Thread

import functions
from functions import  database_value
from functions import increase


if __name__ =="__main__":
    # threads =[]
    # num_threads=10
    #
    #
    # for i in range(num_threads):
    #     if __name__ == '__main__':
    #         thread= Thread(target=functions.square_numbers())
    #         threads.append(thread)
    #
    #
    #
    # for thread in threads :
    #     thread.start()
    #
    #
    # for thread in threads :
    #     thread.join()

    print ('wtart value', database_value)


    thread1 =Thread(target=increase)
    thread2 =Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print ('end value ',functions.database_value)


    print("end MAin ")
