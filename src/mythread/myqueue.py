from queue import Queue
import threading
import time
def job(list, q):

    for i in range(len(list)):
        list[i] = list[i]**2  #平方
    q.put(list)

def multithreading():
    q = Queue()#队列
    threads = []
    results = []
    data = [[3,1,2],[4,5,3],[4,4,4],[5,5,5]]
    for i in range(len(data)):
        t = threading.Thread(target=job, args=(data[i], q))#不能返回数据，放入列表中
        t.start()
        threads.append(t)
    for thread in  threads:
        thread.join()

    for _ in range(4):
        results.append(q.get())

    print(results)

if __name__ == '__main__':
    multithreading()
