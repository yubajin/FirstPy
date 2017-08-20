'''
Created on 2017年8月10日

@author: Administrator
'''
'''
def add(x, y, f):
    return f(x) + f(y)

f=abs
print('函数作为参数', add(3, -4, f))


def format_name(s):
    return s[0].upper()+s[1:].lower()

print (list(map(format_name, ['adam', 'LISA', 'barT'])))

def calc_prod(lst):
    def lazy_calc_prod():
        sum1 = 1
        for ls in lst:
            sum1 = sum1 * ls
        return sum1
    return lazy_calc_prod

f1 = calc_prod([1, 2, 3, 4])
print (f1())'''

from functools import reduce
from datetime import datetime
import functools
# 闭包
# def count():
#     fs = []
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         r = f(i)
#         fs.append(r)
#     return fs
# 
# f1,f2,f3 = count()
# print('f1():',f1())
# print('f2():',f2())
# print('f3():',f3())




# 装饰器一
# def f4(x):
#     return 2 * x
# 
# def new_fn(function, arguments):
#     def fn():
#         print('call first',function.__name__,'()')
#         '''其他要装饰的函数'''
#         return function(arguments)
#     return fn
# 
# 
# g = new_fn(f4,5)
# print(g())
# 
# # 装饰器二
# def new_fn1(function):
#     def fn(arguments):
#         print('call second',function.__name__,'()')
#         return function(arguments)
#     return fn
# 
# f4 = new_fn1(f4)
# print(f4(5))

#======================================================
# 能接收任何参数的通用装饰器
def dec_anyarg(func):
    def wrap(*arg, **kwargs):

        # --- 附加功能 ---
        print("loging i ...")

        return func(*arg, **kwargs)
    return wrap
# 装饰器实践之打印运行时间的函数
def dec_time(function):
    def newfun(arguments):
        t1 = datetime.today()
        r = function(arguments)
        t2 = datetime.today()
        print('call %s in %fs,t1:%s, t2:%s' %(function.__name__, (t2 - t1).seconds, t1, t2))
        return r
    return newfun
 
#可以接受参数的装饰器
def dec_differarg(arg_type):#在外面套了一层
    def dec(f):
        @functools.wraps(f)#自动化完成一些内间方法的复制任务，因为装饰器返回的函数是最里面的函数，而不再是调用者本身函数
        def innerimpl(*args, **kwargs):
            if arg_type == 'int':
                print('arg_type is int')
            elif arg_type == 'string':
                print('arg_type is string')
            else:
                print('arg_type is else')
            return f(*args, **kwargs)
        return innerimpl
    return dec



# L = [1,2,3,4,5]
L = range(1, 5000000)

#按照顺序依次执行装饰器
@dec_anyarg
@dec_time
@dec_differarg(arg_type='int')#arg_type参数可以省略
def comfunc(L):  #1*1+2*2+3*3+...  [1,2,3,4,5]
    def add_(x,y):#相加
        return x + y
    
    def mul(x):#相乘
        return x*x
     
    mul_x_list = list(map(mul,L)) #map后的集合为[1, 4, 9, 16, 25]
    print('1*1+2*2+3*3+4*4+5*5+...: ',reduce(add_,mul_x_list))
    
comfunc(L)
print('comfunc() name: ', comfunc.__name__)
# comfunc = dec_time(comfunc)#重新装饰函数
# comfunc(L)

