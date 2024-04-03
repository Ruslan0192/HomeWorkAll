from threading import Thread
import time

def thread_int():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def thread_str():
    for i in range(ord('a'), ord('k')):
        print(chr(i))
        time.sleep(1)


t1 = Thread(target=thread_int)
t2 = Thread(target=thread_str)

t1.start()
time.sleep(0.5)
t2.start()
t1.join()
t2.join()
