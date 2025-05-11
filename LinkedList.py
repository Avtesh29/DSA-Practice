

class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, val):

        newNode = LLNode(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        
        self.tail.next = newNode
        newNode.prev = self.tail    
        self.tail = newNode

        self.length += 1


    def printList(self):

        curr = self.head
        while curr:
             print(curr.val)
             curr = curr.next

def main():
    my_LL = LinkedList()

    my_LL.append(5)
    my_LL.append(7)
    my_LL.append(10)

    my_LL.printList()
    

if __name__ == '__main__':
    main()
        




