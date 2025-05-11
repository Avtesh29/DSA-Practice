from LinkedList import LLNode, LinkedList

def main():
    my_LL = LinkedList()

    my_LL.append(5)
    my_LL.append(7)
    my_LL.append(10)

    my_LL.printList()

    my_LL.delete(5)

    my_LL.printList()

    my_LL.delete(10)

    my_LL.printList()

    my_LL.delete(7)

    my_LL.printList()

if __name__ == '__main__':
    main()