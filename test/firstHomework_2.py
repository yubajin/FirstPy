'''
1.需要检查输入的数据库字段和值个数是否一一对应
2.在添加操作之前需要检验是否有建表
3.需要检验输入的sql语句是否符合规范

4.支持动态添加表格字段
5.支持建多张表进行操作
6.执行用sql语句进行操作
7、支持算出给定分数列表和权重列表的均值

'''
from test.StackListUtils import *
import re
class mydatabase(object):
    def __init__(self):
        self.__tables = StackListUtils()
        self.__tables.push({})
        self.__fields = []
        self.__id = 0

    def getTables(self):
        return self.__tables

    def setPeekTable(self, table):
        self.__tables.updateLastNode(table)

    def getPeekTable(self):
        return  self.getTables().peek()

    def addTable(self, table):
        self.__tables.push(table)

    def getFields(self):
        return self.__fields

    def setFields(self, fields):
        self.__fields = fields

    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id

    def plusId(self):
        self.__id = self.__id + 1
        return self.__id


    '''
    创建表
    '''
    def create_table(self, fields):#给数据库中创建以传入参数作为字段的表
        self.addTable({})
        self.setId(0)
        self.setFields(fields)
        print('创建表的属性:',self.getFields())

    def add_recode(self, values):
        fields = self.getFields()
        recode = dict(self.getPeekTable())#获得数据库中正在操作的表对象
        recode.setdefault(self.plusId())#id自增,{id:content} content:{'':'','':''...}
        field_value = zip(fields,list(values))#将表的字段和值以键值对的形式打包在一起,需要字段和值严格一一对应
        content = {}
        for (field,value) in field_value:
            content.setdefault(field,value)
        recode[self.getId()] = content
        self.setPeekTable(recode)
        print('一行受影响')

    '''
        传入表的列名列表(字符),分数列表，权重列表，将加权放置给加权列表
    '''
    def calAverage(self, scoreColumn, weightColumn, averageColumn):
        self.alter_table(averageColumn)
        for key, value in dict(self.getPeekTable()).items():
            totalscore = 0
            totalweight = 0
            score_weightLists = zip(scoreColumn, weightColumn)
            for (tempscore, tempweight) in score_weightLists:
                totalscore = totalscore + int(self.getPeekTable()[key][tempscore]) * int(self.getPeekTable()[key][tempweight])
                totalweight = totalweight + int(self.getPeekTable()[key][tempweight])
            average = totalscore / totalweight
            self.getPeekTable()[key][averageColumn] = average
        self.getPeekTable()

    def selectAll(self):
        print('整个数据库:',self.getPeekTable())
        fields_num = self.getFields().__len__()#获取属性个数
        recodeCount = 0#数记录总共条数
        if not fields_num == 0:
            header_wrap = '+---------------' * fields_num + '+---------------+'
            formatStr = '|%-15s' * fields_num + '|%-15s|'
            keys = self.getFields()
            fields = []
            fields.append('id')
            for key in keys:
                fields.append(key)
            header = (formatStr) % (tuple(fields))
            print(header_wrap)
            print(header)
            print(header_wrap)
            for key, value in dict(self.getPeekTable()).items():#遍历每一条记录
                recodeCount = recodeCount + 1
                recodesValue = []
                recodesValue.append(int(key))
                for i in range(1,fields_num + 1):#遍历每条记录的每个属性
                    recodeValue = dict(dict(self.getPeekTable()[key]))[(fields[i])]
                    recodesValue.append(recodeValue)
                result = (formatStr) % (tuple(recodesValue))
                print(result)
            print(header_wrap)
        print("{} rows in database".format(recodeCount))

    def selectById(self):
        pass

    def del_recode(self, id):
        self.getTables().peekDelDicById(id)
        print('一条记录被删除')

    def update_recode(self, id, field, value):
        self.getTables().peekUpdateDicById(id, field, value)

    ''' 
        增加单个数据库字段
        需要将之前的记录该字段置为None
    '''
    def alter_table(self, field):
        fields_num = self.getFields().__len__()  # 获取原来属性个数
        self.getFields().append(field)
        for key, value in dict(self.getPeekTable()).items():  # 遍历每一条记录
            if isinstance(self.getPeekTable()[key],dict):
                self.getPeekTable()[key][(self.getFields()[fields_num])] = None
        print('增加了一个字段')

    def run(self):
        flag = False
        while not flag:
            userinput = input('bajinsql>')
            if(userinput[0:6] == 'create'):
                userinputre = re.search(r'create table (.*)', userinput, re.M | re.I)
                fieldArr = userinputre.group(1).lstrip('(').rstrip(')').replace(' ', '').split(',')
                self.create_table(fieldArr)
            if (userinput[0:6] == 'insert'):
                userinputre = re.search(r'insert (.*) values (.*)', userinput, re.M | re.I)
                fieldArr = userinputre.group(1).lstrip('(').rstrip(')').replace(' ', '').split(',')
                valueArr = userinputre.group(2).lstrip('(').rstrip(')').replace(' ', '').split(',')
                index = 0
                for value in valueArr:
                    tempvalue = eval(value)
                    valueArr[index] = tempvalue
                    index = index + 1

                sentenceMatch = True
                index = 0
                for field in self.getFields():#判断增加记录是用户输入的属性是否和表的属性一致
                    if not field == fieldArr[index]:
                        sentenceMatch = False
                    index = index + 1

                print('用户输入的属性是否和表的属性一致:' ,sentenceMatch)
                if(sentenceMatch):
                    self.add_recode(valueArr)

            elif (userinput[0:6] == 'select'):
                if (userinput == 'select * from database'):
                    self.selectAll()
                elif (userinput == 'select * from database sortby average'):
                    pass

            elif (userinput[0:6] == 'delete'):
                userinputre = re.search(r'delete (.*) where (.*)', userinput, re.M | re.I)
                delId = int(userinputre.group(2).replace(' ', '').split('=')[1])
                self.del_recode(delId)

            elif (userinput[0:6] == 'update'):
                userinputre = re.search(r'update database set (.*) where (.*)', userinput, re.M | re.I)
                keys_values = userinputre.group(1).replace(' ', '').split(',')
                keys = []
                values = []
                for key_value in keys_values:#获取用户输入的属性和属性的值
                    keys.append(key_value.split('=')[0])#属性
                    values.append(key_value.split('=')[1])#属性的值
                tempkeys_values = zip(keys,values)
                updateId = int(userinputre.group(2).replace(' ', '').split('=')[1])
                countField = 0
                for key,value in tempkeys_values:
                    self.update_recode(updateId,key,eval(value))
                    countField = countField + 1
                print('一条记录的' + str(countField) + '个属性值已经更改')
            #alter database add average
            elif (userinput[0:5] == 'alter'):
                userinputre = re.search(r'alter database add (.*)', userinput, re.M | re.I)
                addField = userinputre.group(1).replace(' ', '')
                self.alter_table(addField)
            elif (userinput == 'exit()'):
                flag = True

db = mydatabase()
db.create_table(['name','guowen_score','guowen_weight','math_score','math_weight'])
db.add_recode(['zhangshang',89,2,94,3])#需要检查创建表的属性要与增加记录的值的个数一一对应
db.add_recode(['lisi',87,2,98,3])#需要检查创建表的属性要与增加记录的值的个数一一对应
# db.del_recode(1)
db.update_recode(2,'name','changed')#需要检查要更改的属性是否在表里存在
db.calAverage(['guowen_score','math_score'],['guowen_weight','math_weight'],'average')
db.selectAll()

# db.alter_table('average')
# db.add_recode(['wangwu',78,3,90,2,85.8])
# db.selectAll()
db.run()

# print(dict(db.getPeekTable()))
# create table (name,guowen_score,guowen_weight,math_score,math_weight)
# insert (name,guowen_score,guowen_weight,math_score,math_weight) values ('zhangshagn',94 ,2,84,3)
# insert (name,guowen_score,guowen_weight,math_score,math_weight) values ('lisi',89 ,2,96,3)
#
# select * from database
# select * from database sortby average
#delete database where id = 2
#update database set name = 'haschange', guowen_score = 60, math_score = 70 where id = 1

#create table (name1,guowen_score1,guowen_weight1,math_score1,math_weight1)
# insert (name1,guowen_score1,guowen_weight1,math_score1,math_weight1) values ('wanglaowu_1',94,4 ,84,7)



