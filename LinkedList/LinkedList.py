
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


    def append(self, val) -> LLNode:
        '''
        Append a node with speicified value to the end of the linked list,
        return node that was added.
        '''
        newNode = LLNode(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return newNode
        
        self.tail.next = newNode
        newNode.prev = self.tail    
        self.tail = newNode

        self.length += 1
        return newNode


    def find(self, val) -> LLNode:
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
    

    def delete(self, val) -> LLNode:
        '''
        Delete the first occurence of a node from linked list,
        return the node or None if not found.
        '''
        delNode = self.find(val)
        if not delNode:
            return None
        
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
    

    def insertAtIndex(self, index, val) -> bool:
        '''
        Insert node with value at a certain index if in bounds,
        Return bool indicating success or failure
        '''
        if index < 0 or index >= self.length:
            return False

        if self.length == 0:
            self.append(val)    # Append to empty list
            return True

        newNode = LLNode(val)
        curr = self.head

        if index == 0:
            newNode.next = curr
            curr.prev = newNode
            self.head = newNode
            self.length += 1
            return True

        i = 0
        while i < index:
            curr = curr.next
            i += 1
        
        curr.prev.next = newNode
        newNode.prev = curr.prev
        curr.prev = newNode
        newNode.next = curr
        self.length += 1
        return True
            
        

    def printList(self) -> None:
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
        




