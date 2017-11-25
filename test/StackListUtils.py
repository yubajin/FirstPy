
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

    def updateLastNode(self,val):
        tempNode = StackListUtils.header
        if tempNode.get_next() == None:
            return
        tempNode.set_val(val)

    def isEmpty(self):
        if(StackListUtils.header.get_next() == None):
            return True
        else:
            return False

    def clear(self):
        StackListUtils.header = StackListUtils.Node(None)

    def getAllNode(self):
        pass


# a = StackListUtils()
# a.push(2)
# a.push(4)
# a.push(5)
# a.push({'id':1,'name':2})
# a.push(6)
# a.updateLastNode(90)
# # a.clear()
# print(a.peek())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.isEmpty())
# print(a.pop())
# print(a.pop())