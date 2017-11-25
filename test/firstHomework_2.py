from test.StackListUtils import *
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
        self.__fields = list(fields)

    def getId(self):
        return self.__id

    def plusId(self):
        self.__id = self.__id + 1
        return self.__id


    '''
    创建表
    '''
    def create_table(self, *fields):#给数据库中创建以传入参数作为字段的表
        self.setFields(fields)
        # recode = dict(self.getTables().peek())#获得数据库中正在操作的表对象
        # recode.setdefault(self.plusId())#id自增,{id:content} content:{'':'','':''...}
        # content = {}
        # for field in fields:
        #     content.setdefault(field)
        # recode[self.getId()] = content
        # self.setPeekTable(recode)

    def add_recode(self, table, *values):#table=self.getTables().peek()
        fields = self.getFields()
        recode = dict(table)#获得数据库中正在操作的表对象
        recode.setdefault(self.plusId())#id自增,{id:content} content:{'':'','':''...}

        field_value = zip(fields,list(values))#将表的字段和值以键值对的形式打包在一起
        content = {}
        for (field,value) in field_value:
            content.setdefault(field,value)
        recode[self.getId()] = content
        self.setPeekTable(recode)

    def selectAll(self):
        pass

    def selectById(self):
        pass

    def del_recode(self):
        pass

    def update_recode(self):
        pass

    def alter_table(self):
        pass

    def run(self):
        pass

db = mydatabase()
db.create_table('name','guowen_score','math_score')
db.add_recode('zhangshang',89,94)

print('db.getFields()',db.getFields())
print('db.getPeekTable()',db.getPeekTable())

