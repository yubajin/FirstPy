import threading

def thread_job():
    print('This is an added Thread,number is %s' % threading.current_thread())


def main():
    add_thread = threading.Thread(target=thread_job)
    add_thread.start()
    print('threading active_count:',threading.active_count())#查看开通线程个数
    print('threading.enumerate:', threading.enumerate());#查看开通哪几个线程
    print('current_thread:',threading.current_thread())#正在运行的线程
    print('main_thread:',threading.main_thread())
    print('get_ident:',threading.get_ident)

if  __name__  == '__main__':
    main()