import threading
import time
from datetime import datetime

def thread_job():
    print('T1 is started at %s' % datetime.today())
    for i in range(10):
        time.sleep(0.1)
    print(r'T1 is finished at %s' % datetime.today())

def T2_job():
    print(r'T2 is start at %s' % datetime.today())
    time.sleep(0.9)
    print(r'T2 is finished at %s' % datetime.today())

def main():
    add_thread = threading.Thread(target=thread_job,name='T1')
    thread2 = threading.Thread(target=T2_job,name='T2')
    add_thread.start()
    thread2.start()

    # 加入主线程，这个程序运行完之后才结束主程序，这个程序运行的同时不会阻塞其他线程运行
    # 如果加入主程序的这个程序运行时间比其他程序时间都长，那么所有程序都结束后主程序才能结束
    # 如果加入主程序的这个程序运行时间不是最长，那么他执行结束后不管其他运行时间更长的程序，主程序就结束
    add_thread.join()

    print(r'all dona at %s' % datetime.today())
    # print('threading active_count:',threading.active_count())#查看开通线程个数
    # print('threading.enumerate:', threading.enumerate());#查看开通哪几个线程
    # print('current_thread:',threading.current_thread())#正在运行的线程
    # print('main_thread:',threading.main_thread())
    # print('get_ident:',threading.get_ident)

if  __name__  == '__main__':
    main()