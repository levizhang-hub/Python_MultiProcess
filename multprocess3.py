#encoding:utf-8
import multiprocessing as mp
import time

def job(v,num,l):
    l.acquire()
    for _ in range(10):
        time.sleep(num)
        v.value+=num
        print(v.value) 
    l.release()


if __name__=="__main__":
    l=mp.Lock()
    v=mp.Value('i',0)
    p1=mp.Process(target=job,args=(v,1,l))
    p2=mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()