#  Linked List Procedure
#  linked list consists of nodes .

class node:

    def __init__(self,data):
        self.data = data
        self.next = None

# Creating linked LIst
# and each link list will start with head node

class linkedList:

    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode

    def print(self):
        temp = self.head

        while temp :
            print(temp.data, end = "--->")
            temp = temp.next

        print("\n")

    def reversePrint(self) :

        temp = self.head
        reverse = linkedList()

        while temp:
            reverse.push(temp.data)
            temp = temp.next

        reverse.print()

# create Object of class LinkedLIst

list1 = linkedList()

list1.push(1)
list1.push(2)
list1.push(3)

list1.print()
list1.reversePrint()