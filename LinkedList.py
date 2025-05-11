

class LLNode:
    '''
    Class to represent a doubly linked list node. Contains a value and
    a pointer to next or previous nodes. Not circularly linked
    '''
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    '''
    Class to represent the entire doubly linked list. Contains pointer to 
    the head and the tail to allow for quick operations. 
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, val):
        '''
        Append a node with speicified value to the end of the linked list,
        return node that was added.
        '''
        newNode = LLNode(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        
        self.tail.next = newNode
        newNode.prev = self.tail    
        self.tail = newNode

        self.length += 1


    def find(self, val):
        '''
        Find and return the first occurence of a node given a value,
        return None if node not found.
        '''
        curr = self.head

        while curr:
            if curr.val == val:
                return curr
            curr = curr.next

        return None
    

    def delete(self, val):
        '''
        Delete the first occurence of a node from linked list,
        return the node or None if not found.
        '''
        delNode = self.find(val)
        
        if delNode == self.head:
            self.head = delNode.next
            
        elif delNode == self.tail:
            delNode.prev.next = None
            self.tail = delNode.prev
        
        if delNode.next:
            delNode.next.prev = delNode.prev\
            
        if delNode.prev:
            delNode.prev.next = delNode.next
        
        self.length -= 1
        return delNode



    def printList(self):
        '''
        Iterate through list and print every node's value,
        return nothing
        '''
        curr = self.head
        if curr and self.tail:
            print("Head:", curr.val, " Tail:", self.tail.val, " Length:", self.length)

        while curr:
             print(curr.val, end=' ')
             curr = curr.next
        print()
        




