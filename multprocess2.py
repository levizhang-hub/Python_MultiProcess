#encoding:utf-8
import multiprocessing as mp
import time

def job(x):
    return x*x



if __name__=="__main__":
    pool=mp.Pool(processes=8)
    res=pool.map(job,range(10))
    print(res)
    
    res=pool.apply_async(job,(2,))
    print(res.get())
     
    mult_res=[pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in mult_res] )