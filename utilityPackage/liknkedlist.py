
class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
        # print(data)


class LinkedList:

    def __init__(self):
        self.head = None
        return


    def addNode(self, newNode):
        #print(newNode)
        # print(self.head , newNode)
        if self.head is None :
            self.head = newNode
            # print(self.head , newNode)
        else :
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else :
                    lastNode = lastNode.next
            lastNode.next = newNode
        return

    def printLinkedList(self):
        currentNode = self.head
        while True :
                if currentNode is None :
                    break
                else :
                    print("{" , currentNode.data , " , " , currentNode.next , "}")
                    currentNode = currentNode.next
        return
    # def remove(self):


myList = LinkedList()
# myList.addNode(15)
# myList.addNode(12)
# list = []
# with open('textFile.txt','r') as f:
#     for line in f:
#         for word in line.split():
#             list.append(word)
#            # print(word)
# #print(list)
# for i in range(0,len(list)) :
#     data = list[i]
#     myList.addNode(data)
    #print(list[i])
node1 = Node(15)
ll = LinkedList()
ll.addNode(node1)

node2 = Node("Akanksha")
ll1 = LinkedList()
ll1.addNode(node2)




#