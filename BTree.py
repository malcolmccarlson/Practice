import argparse


def btreecli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--addnode", nargs='+', help="add node to B-Tree")
    args = parser.parse_args()
    nodes = args.addnode
    nodeList = []
    for nodes in parser.parse_args()._get_kwargs():
       nodeList.append(nodes) 
    return nodeList[0][1]


class Node:

    def __init__(self, key):
        self.left = left
        self.right = right
        self.val = key

    def buildTree(self,data): 
        llength = len(data)
        root = data[0]
        print(root)

def main():
     newnodes = btreecli()
     print(newnodes)
     newTree = Node.buildTree(newnodes)

if __name__ == '__main__':        
    main() 

