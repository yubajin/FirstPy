
class StackListUtils(object):

    class Node(object):
        def __init__(self, val):
            self.__val = val
            self.__next = None
        def get_val(self):
            return self.__val
        def set_val(self, val):
            self.__val = val
        def get_next(self):
            return self.__next
        def set_next(self, next):
            self.__next = next

    header = Node(None)

    def push(self,val):
        pushNode = self.Node(val)
        pushNode.set_next(StackListUtils.header)
        StackListUtils.header = pushNode

    def pop(self):
        popNode = StackListUtils.header
        if popNode.get_next() == None:
            return
        else:
            StackListUtils.header = StackListUtils.header.get_next()
            return popNode.get_val()

    def peek(self):
        popNode = StackListUtils.header
        if popNode.get_next() == None:
            return
        else:
            return popNode.get_val()

    #delete
    '''
        如果最后一个元素是一个字典，删除字典里面的某条数据
    '''
    def peekDelDicById(self, id):
        if isinstance(StackListUtils.header.get_val(),dict):
            StackListUtils.header.get_val().pop(int(id))
        else:
            print('栈的最后一个元素不是字典')
        return  StackListUtils.header.get_val()

    #updata
    def updateLastNode(self, val):
        tempNode = StackListUtils.header
        if tempNode.get_next() == None:
            return
        StackListUtils.header.set_val(val)

    '''
        如果最后一个元素是一个字典，更改字典里面的某条数据
    '''
    def peekUpdateDicById(self, id, field, value):
        if isinstance(StackListUtils.header.get_val()[int(id)], dict):
            tempdict = {field:value}
            StackListUtils.header.get_val()[int(id)].update(tempdict)

    def isEmpty(self):
        if(StackListUtils.header.get_next() == None):
            return True
        else:
            return False

    def clear(self):
        StackListUtils.header = StackListUtils.Node(None)

    def getAllNode(self):
        pass

