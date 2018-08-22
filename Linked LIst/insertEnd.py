class Node(object):

    def __init__(self,data):
        self.data=data
        self.nextNode=None

class linkedlist(object):

    def __init__(self):
        self.head=None
        self.size=0

    def insertStart(self,data):
        self.size+=1
        newNode=Node(data)

        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def insertEnd(self,data):
        self.size+=1
        newNode=Node(data)
        actualNode=self.head
        while(actualNode.nextNode is not None):
            actualNode=actualNode.nextNode
        actualNode.nextNode=newNode

    def traverse(self):
        actualNode=self.head
        while(actualNode is not None):
            print(actualNode.data)
            actualNode=actualNode.nextNode

    def size(self):
        return self.size