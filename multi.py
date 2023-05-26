# from multiprocessing import Process
from threading import  Thread, Lock
import os
import time
from queue import Queue


# def square_num():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)

# global variable
# database_val = 0

# def increase(lock):
#     global database_val

#     lock.acquire()
#     local_copy = database_val

#     # processing
#     local_copy += 1
#     time.sleep(0.1)
#     database_val = local_copy
#     lock.release()




# # processes = []
# # num_processes = os.cpu_count()
# # print(num_processes)

# # Threading




# # create processes
# if __name__ == "__main__":
#     # p = Process(target=square_num)
#     # threads = []
#     # num_threads = 10
#     # for i in range(num_threads):
#     #     t = Thread(target=square_num)
#     #     threads.append(t)

#     # # start each process
#     # # p.start()
#     # for t in threads:
#     #     t.start()

#     # # Join
#     # # p.join()
#     # for t in threads:
#     #     t.join()


#     lock = Lock()
#     print('start value', database_val)

#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))

#     # Start each thread
#     thread1.start()
#     thread2.start()

#     # Join each tread after excution
#     thread1.join()
#     thread2.join()

#     print("end value", database_val)
#     print('end main')


# Queues
if __name__ =="__main__":
    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)

    first = q.get()
    print(first)

    # check