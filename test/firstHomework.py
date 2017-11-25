database = [{} for n in range(0,100)]
dataid=0

def init():
    for recode in database:
        temp = {
                        'name':'',
                        'subject':
                            {
                                'guowen':{'score':0,'weight':2},
                                'math':{'score':0,'weight':3}
                            } ,
                        'average':0
                    }
        recode.update(temp)

def calSingleAverage(index):
    totalscore = (database[index]['subject']['guowen']['score'] * database[index]['subject']['guowen']['weight']
        + database[index]['subject']['math']['score'] * database[index]['subject']['math']['weight'])
    totalweight = database[index]['subject']['guowen']['weight'] + database[index]['subject']['math']['weight']
    average = totalscore / totalweight
    database[index]['average'] = average

def calAverage():
    for recode in database:
        totalscore = (recode['subject']['guowen']['score'] * recode['subject']['guowen']['weight']
                      + recode['subject']['math']['score'] * recode['subject']['math']['weight'])
        totalweight = recode['subject']['guowen']['weight'] + recode['subject']['math']['weight']
        average = totalscore / totalweight
        recode['average'] = average


def addName(name):
    global dataid
    dataid = dataid + 1
    temIndex = 0
    for recode in database:
        if(recode['name']==''):
            index = temIndex
            recode['dataid'] = dataid
            break
        else:
            temIndex = temIndex + 1
    database[index]['name'] = name
    return index

def addScore(index, guowen, math):
    database[index]['subject']['guowen']['score'] = guowen
    database[index]['subject']['math']['score'] = math
    database[index]['subject']['guowen']['weight'] = 2
    database[index]['subject']['math']['weight'] = 3
    calSingleAverage(index)

def add(name,guowen,math):
    index = addName(name)
    addScore(index, guowen, math)

def delete():
    pass

def update():
    pass

def selectAll():
    pass

def sortByName():
    pass

def sortByAverage():
    pass

init()
index = addName('yubajin')
addScore(index,86,94)
index = addName('yingmingming')
addScore(index,98,99)
print(database)