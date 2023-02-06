# 1st i have to create the class node
#  2nd - then i have to create the class link list
#  3rd - then i have to create method of linked list like  

# METHODS - 
# 1 - ADD NODE AT START AND END , 2- DEL NODE, 3- PRINT NODE FROM START AND END , 4- ADD NODE AFTER DASH DASH DASH NODE ,

# 4TH - for future developement we will make an another class called "COding problems", where we will type interesting methods based on linked list


class node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def changeValue(self, value):
        self.value = value

    def changeNext(self,next):
        self.next = next


class linkedList:

    def __init__(self,head = None,tail=None):
        self.head = head
        self.tail = tail

# Adding Nodes 
    def addNode(self,value):
        newNode= node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
            
        self.tail.next = newNode
        self.tail = newNode

    def addNodeAtStart(self,value):
        # create a new node
        # change head value to new node
        # put the next value of head to the previous head

        prev = self.head
        newNode = node(value)

        self.head = newNode
        newNode.next = prev
        print("Value added at start successFully")

    def addNodeAtEnd(self,value):
        self.addNode(value)
        print("Value added at end successFully")

# Add Node after dash node

    def addNodeAfter(self,value,newValue):
        newNode= node(newValue)
        temp = self.head

        while temp is not None:

            if temp.value == value:
                newNode.next = temp.next
                temp.next = newNode
                return
            
            temp = temp.next

# Delete Node
    def deleteNode(self,value):
        
        temp = self.head
        if temp.value == value:
            self.head = temp.next
            return
            
        prev = None

        while temp is not None:

            if temp.value == value:
                prev.next = temp.next
                
            prev = temp
            temp = temp.next

    
# Print
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end='-->')
            temp = temp.next

        print("\n")

    def printReverse(self):
        pass



Node1 = node(5)
Node2 = node(10)
Node3 = node(20)
Node4 = node(40)

ll1 = linkedList()

ll1.addNode(5)
ll1.addNode(10)
ll1.addNode(20)
ll1.addNode(40)
ll1.addNode(80)
ll1.addNode(160)
ll1.addNodeAtStart(1)
ll1.addNodeAtEnd(320)
# ll1.deleteNode(80)
ll1.addNodeAfter(1,3)


ll1.print()


# print(finalPrint)


            


# i want to check whether my node class is working or not
# 2 then i want to check whether my linked list is working or not
#  3 then i will create node and will add that in linked list