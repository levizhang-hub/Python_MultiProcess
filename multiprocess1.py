#encoding:utf-8
import multiprocessing as mp
import threading as td
import time
from queue import Queue

def job1(q):
    res=0
    for i in range(100000000):
        res += i+i**2+i**3
    q.put(res)
 

def multcore(): 
    q=mp.Queue()
    p1=mp.Process(target=job1,args=(q,))
    p2=mp.Process(target=job1,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    res1=q.get()
    res2=q.get()
    print('multicore: ',res1+res2)
    
def multthread(): 
    q=Queue()
    t1=td.Thread(target=job1,args=(q,))
    t2=td.Thread(target=job1,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    res1=q.get()
    res2=q.get()
    print('multthread: ',res1+res2)
    
def normal():
    res=0
    for _ in range(2):
        for i in range(100000000):
            res+=i+i**2+i**3
    print('normal: ',res)
    
if __name__=='__main__':
    s_t=time.time()
    normal()
    print('normal time is: ',time.time()-s_t)
    s_t=time.time()
    multthread()
    print('multthread time is: ',time.time()-s_t)
    s_t=time.time()
    multcore()
    print('multcore time is: ',time.time()-s_t)
   