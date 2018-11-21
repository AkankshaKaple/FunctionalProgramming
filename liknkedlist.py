
class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
        print(data)


class LinkedList:
        #print(data)
    def __init__(self, head = None):
        #print(self.data)
        self.head = head
        self.lastNode = None
        self.size = 0


    def addNode(self, data):
        #print(self.data)
        newNode = Node(data) # Creating Node class object to initialize node with data

        if self.head is None :
                self.head = newNode
        else :
            self.lastNode = self.head
            while True:
                if self.lastNode.next is None:
                    break
                else :
                    self.lastNode = self.lastNode.next
                    self.lastNode.next = newNode

    def printLinkedList(self):
        currentNode = self.head
        while True :
                if currentNode == None :
                    break
                print(currentNode.data)
                currentNode = currentNode.next

myList = LinkedList()
# myList.addNode(15)
# myList.addNode(12)
list = []
with open('textFile.txt','r') as f:
    for line in f:
        for word in line.split():
            list.append(word)
           # print(word)
#print(list)
for i in range(0,len(list)) :
    data = list[i]
    myList.addNode(data)
    #print(list[i])
# node = LinkedList()
# node.head = Node(12)
# node.head.next = Node(1)
# node3 = Node(9)
# node2.next = node3