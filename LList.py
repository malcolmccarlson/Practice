import argparse


def llcli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--append", type=str, default=None, help="append to end of linked list")
    parser.add_argument("--llist", type=bool, default=False, help="list contest of linked list")
    parser.add_argument("--lprint", type=bool, default=False, help="print Linked List contents")
    args = parser.parse_args()
    appendStr = args.append
    listStr = args.llist
    printList = args.lprint
    return appendStr, listStr, printList

def main():
    appVal, listlist, lp= llcli()
    llist1 = LinkedList()
    if listlist is True:
        llist1.listAppend(appVal)
    if lp is True: 
        llist1.printList()


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def listAppend(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def prepend(self, data):
        self.head = Node(data=data, next=self.head)

    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data) 
            temp = temp.next



if __name__ == '__main__':
    main()        
