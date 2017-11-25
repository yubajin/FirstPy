import re

class myDataBase(object):
    def __init__(self, database={}, dataid=0):
        self.database = database
        self.dataid = dataid

    def get_database(self):
        return self.database

    def get_dataid(self):
        return self.dataid

    def set_database(self,database):
        self.database = database

    def set_dataid(self, dataid):
        self.dataid = dataid

    def calSingleAverage(self, index):
        totalscore = (int(self.get_database()[index]['subject']['guowen']['score']) * int(self.get_database()[index]['subject']['guowen']['weight'])
            + int(self.get_database()[index]['subject']['math']['score']) * int(self.get_database()[index]['subject']['math']['weight']))
        totalweight = self.get_database()[index]['subject']['guowen']['weight'] + self.get_database()[index]['subject']['math']['weight']
        average = totalscore / totalweight
        self.get_database()[index]['average'] = average

    def add(self, name,guowen_score,math_score):
        self.set_dataid(self.get_dataid() + 1)

        recode={}
        recode['name'] = name
        recode['subject'] = {
                                    'guowen':{'score':guowen_score,'weight':2},
                                    'math':{'score':math_score,'weight':3}
                              }
        recode['average'] = 0
        self.get_database()[self.get_dataid()] = recode
        self.calSingleAverage(self.get_dataid())

    def delete(self, id):
        self.get_database().pop(id)

    def update(self, id,name,guowen_score,math_score):
        insertedrecode = self.seleteId(id)
        if(not name  == ''):
            insertedrecode['name'] = name
        if(not guowen_score == ''):
            insertedrecode['subject']['guowen']['score'] = guowen_score
        if(not math_score == ''):
            insertedrecode['subject']['math']['score'] = math_score
        inserteddatabase = {id:insertedrecode}
        self.get_database().update(inserteddatabase)
        self.calSingleAverage(id)

    def seleteId(self, id):
        return self.get_database()[id]

    def seleteAll(self, selectDatabase):
        header_wrap = '+---------------+---------------+---------------+---------------+---------------+---------------+---------------+'
        header = ("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|" % (
            "id", "name", "guowen_score", "guowen_weight", "math_score", "math_weight", "average"))
        print(header_wrap)
        print(header)
        print(header_wrap)

        exitIndex = 0
        for key,value in selectDatabase.items():
            exitIndex = exitIndex + 1
            name = str(value['name']).strip("'")
            guowen_score = value['subject']['guowen']['score']
            guowen_weight = value['subject']['guowen']['weight']
            math_score = value['subject']['math']['score']
            math_weight = value['subject']['math']['weight']
            average = value['average']

            result = ("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|" % (
                key, name, guowen_score, guowen_weight, math_score, math_weight, average))

            print(result)
        print(header_wrap)
        print("{} rows in database".format(exitIndex))

    def sortBy(self):
        return dict(sorted(self.get_database().items(), key=lambda x: x[1]['average'], reverse=True))

    def selectByAver(self):
        sorteddata = self.sortBy()
        self.get_database().update(sorteddata)
        self.seleteAll(sorteddata)

    def run(self):
        flag = False
        while not flag:
            userinput = input('bajinsql>')

            if(userinput[0:6] == 'insert'):
                userinputre = re.search(r'insert (.*) values (.*)', userinput, re.M | re.I)
                attrArr = userinputre.group(1).lstrip('(').rstrip(')').replace(' ', '').split(',')
                valueArr = userinputre.group(2).lstrip('(').rstrip(')').replace(' ', '').split(',')
                if(attrArr[0]=='name' and attrArr[1]=='guowen_score' and attrArr[2]=='math_score'):
                    self.add(valueArr[0], valueArr[1], valueArr[2])

            elif(userinput[0:6]=='delete'):
                userinputre = re.search(r'delete (.*) where (.*)', userinput, re.M | re.I)
                delId = int(userinputre.group(2).replace(' ', '').split('=')[1])
                self.delete(delId)

            elif(userinput[0:6] == 'select'):
                if(userinput=='select * from database'):
                    self.seleteAll(self.get_database())
                elif (userinput == 'select * from database sortby average'):
                    self.selectByAver()

            elif(userinput[0:6] == 'update'):
                userinputre = re.search(r'update (.*) set (.*) where (.*)', userinput, re.M | re.I)
                recode = userinputre.group(1).replace(' ', '')
                attrMapArr = userinputre.group(2).replace(' ', '').split(',')
                update_name = attrMapArr[0].split('=')[1]
                update_guowen_score = attrMapArr[1].split('=')[1]
                update_math_score = attrMapArr[2].split('=')[1]
                updateId = int(userinputre.group(3).replace(' ', '').split('=')[1])
                self.update(updateId,update_name,update_guowen_score,update_math_score)

            elif(userinput == 'exit()'):
                flag = True

mydata = myDataBase()
mydata.run()
# add('zhangshan',99 ,78)
# add('lisi',100 ,98)
# add('yubajin',89 , 88)
# add('waolaowu',83 , 96)
# seleteAll(database)
# selectByAver()

# insert (name,guowen_score,math_score) values ('yubajin',89 , 88)
# insert (name,guowen_score,math_score) values ('zhangshan',99 ,89)
# insert (name,guowen_score,math_score) values ('lisi',87 ,77)
# insert (name,guowen_score,math_score) values ('wanglaowu',94 ,84)
# select * from database
# select * from database sortby average
#delete database where id = 2
#update database set name = 'haschange', guowen_score = 60, math_score = 70 where id = 1