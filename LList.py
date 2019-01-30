def llcli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--append", nargs='+', help="append to end of linked list")
    parser.add_argument("--lprint", type=bool, default=False, help="print Linked List contents")
    args = parser.parse_args()
    append = args.append
    appList = []
    for append in parser.parse_args()._get_kwargs():
       appList.append(append) 
    printList = args.lprint
    return appList, printList

def takeNodes(nodeList):
    llist1 = LinkedList()
    for node in nodeList:
       llist1.listAppend(node)
    return llist1

def main():
    appVals, lp= llcli()
    nlist = takeNodes(appVals)
    if lp is True: 
        nlist.printList()


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
