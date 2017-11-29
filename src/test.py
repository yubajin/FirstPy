# -*- coding: UTF-8 -*-
import re
using_db = {
            "user": {
                        'name': {}, 'chinese': {}, 'math': {}, 'chinese_weight': {}, 'math_weight': {}, 'all_grade': {}
                    },
            "user_count":0
           }

# 方法区域
#insert into user(name,chinese,math,chinese_weight,math_weight) values(1,2,3,4,5);
def insert(command):
    pattern = validate(command, "insert")
    if (pattern != None):
        table_name = pattern.group(1)
        table_columns = pattern.group(2).split(",")
        values = pattern.group(3).split(",")
        if (len(values) != len(table_columns)):
            print("列表数与参数个数不同")
        elif (table_name not in using_db):
            print("数据库中没有该表")
        else:
            column_values = list(zip(table_columns, values))
            column_values.append(("all_grade",int(column_values[1][1])*int(column_values[3][1])
                                            + int(column_values[2][1])*int(column_values[4][1])))
            list(
                map(lambda data :
                        using_db["user"][data[0]].__setitem__(using_db["user_count"],data[1])
                        if data[0] == "name" else
                        using_db["user"][data[0]].__setitem__(using_db["user_count"],int(data[1]))
                    ,column_values)
                 )
            using_db["user_count"] += 1
    else:
        print("指令错误")


def select(command):
    pattern = validate(command, "select")
    if (pattern != None):
        results = pattern.groups()
        table = results[0]
        keys = list(using_db[table].keys())
        selects = []
        selects = list(
                    map(lambda x:
                                tuple(
                                    map(lambda y:
                                        using_db[table][y[0]][y[1]]
                                        ,list(zip(keys,[x] * len(keys)))
                                        )
                                    )
                        ,using_db[table][keys[0]].keys())
                       )
        if(len(results) >= 2):
            selects = selectsort(results,table,keys,selects)
        print(selects)
    else:
        print("指令错误")


def selectsort(results,table,keys,selects):
        sort_column_and_sort_type = results[1]
        sorts = sort_column_and_sort_type.split(" ")
        sort_column = sorts[0];
        sort_type = "desc"
        if(len(sorts) == 2):
            sort_type = sorts[1]
        is_desc = False
        if(sort_type == "desc"):
            is_desc = True
        elif(sort_type == "asc"):
            is_desc = False
        else:
            print("指令错误,排序方式只有desc 和 asc 没有 " + sort_type)
        if(sort_column in using_db[table]):
            selects = sorted(selects
                             ,key = lambda x : x[keys.index(sort_column)]
                             ,reverse = is_desc)
        else:
            print("排列所依据的列不存在该表中")
        return selects
#update us
def update(command):
    pattern = validate(command, "update")
    if (pattern != None):
        params = pattern.groups()
        table = params[0]
        update_column = params[1]
        update_column_value = params[2]
        if (len(params) == 3):
            updateAll(table, update_column, update_column_value)
        else:
            where_column = params[3]
            where_column_value = params[4]
            updatePart(table, update_column, update_column_value, where_column, where_column_value)


def updateAll(table, update_column, update_column_value):
    if (update_column in using_db[table]):

        keys = using_db[table][update_column].keys()
        list(
            map(
                lambda index:
                using_db[table][update_column].__setitem__(index,update_column_value)
                if update_column == "name"
                else using_db[table][update_column].__setitem__(index,int(update_column_value))
                ,keys)
             )
    else:
        print("不存在该字段" + update_column)


def updatePart(table, update_column, update_column_value, where_column, where_column_value):
    if (table in using_db):
        if (update_column in using_db[table]):
            list_where = where(table, where_column, where_column_value)
            list(
                map(
                    lambda index :
                    using_db[table][update_column].__setitem__(index,update_column_value)
                    if update_column == "name"
                    else using_db[table][update_column].__setitem__(index,int(update_column_value))
                    ,list_where))
        else:
            pass
    else:
        pass


def where(table, where_column, where_column_value):
    list_where = []
    if (where_column in using_db[table]):
        counts = using_db[table][where_column].keys()
        print(counts.__str__() + ":" + where_column + ":" + where_column_value)
        list_where = list(
                            filter(lambda index :
                              str(using_db[table][where_column][index]) == where_column_value
                              ,counts
                              )
                          )
        print(list_where)
    return list_where


def delete(command):
    pattern = validate(command, "delete")
    if (pattern != None):
        table = pattern.group(1)
        where_column = pattern.group(2)
        where_column_value = pattern.group(3)
        list_where = where(table, where_column, where_column_value)

        list(map(
                lambda index :
                        list(
                            map(lambda key,i :
                                using_db[table][key].pop(i)
                                ,using_db[table].keys(),[index] * len(using_db[table].keys())
                                )
                            )
                ,list_where)
            )


def validate(command, type):
    p1 = ""
    if (type == "insert"):
        p1 = '^insert into (.*)\((.*)\) values\((.*)\);$'
    elif (type == "select"):
        result = re.search("^select \* from (.*) by (.*)?;$",command)
        if(result != None):
            return result
        p1 = "^select \* from (.*);$"
    elif (type == "update"):
        # update user set name = 10,a = 11 where name = 'jk'
        result = re.search("^update (.*) set (.*) = (.*) where (.*) = (.*);$",command)
        if(result != None):
            return result
        p1 = "^update (.*) set (.*) = (.*);$"
    elif(type == "delete"):
        p1 = "^delete (.*) where (.*) = (.*);$"
    return re.search(p1, command)


# 主函数
while True:
    command = input("请输入指令\n")
    commands = command.split(' ')
    if (commands[0] == 'select'):
        select(command)
    elif (commands[0] == 'insert'):
        #insert into user(name,chinese,chinese_weight,math_weight,chinese_grade,math_grade) values(1,2,3,4,5,6);
        insert(command)
    elif (commands[0] == 'update'):
        update(command)
    elif (commands[0] == 'delete'):
        delete(command)
    else:
        print("对不起，输入错误")
    print(using_db)