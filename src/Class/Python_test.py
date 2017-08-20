'''
Created on 2017年8月7日
重写方法__str__对应print()方法, __dir__

创造一个对象，先用__init__函数实例化，然后调用__setattr__给属性赋值，赋值一个属性，调用一下函数
@author: Administrator
'''
class Programer(object):
    
    def __init__(self,name,age):
        print('I\'m creating myself!')
        self.name = name
        if isinstance(age, int):
            self.age= age
        else:
            raise Exception('age must be int')
        
    def __str__(self):
        return '%s is %s years old' %(self.name, self.age)
    
    def __dir__(self):
        return self.__dict__.keys()
    
    def __setattr__(self,name,value):
        print('I\'m setting attribute')
        self.__dict__[name] = value
        print(name,':',self.__dict__[name])
        
    def __getattribute__(self,name):
        print('I\'m getting attribute')
        return super(Programer,self).__getattribute__(name)
    
if __name__ == '__main__':  
    p = Programer('albert',25)
    print (p)
    print (dir(p))
