'''
Created on 2017年8月7日

@author: Administrator
'''
class Programer(object):
    hobby = 'Play Computer'
    
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight
        
    def get_weight(self):
        return self.__weight
    
if __name__ == '__main__':
    programer = Programer('YuBajin',20,56)
    print (dir(programer))
    print(programer.__dict__)