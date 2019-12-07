# make a linked list

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp= temp.next

    def push(self,new_data):
        new_node = Node(new_data)

        new_node.next= self.head
        self.head = new_node

    def afterInsert(self,new_data,prev_node):

        new_node = Node(new_data)
        if prev_node is None:
            print("node should be in linked list")
            return

        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

if __name__ == "__main__":

    list_one = LinkedList()

    list_one.push(6)
    list_one.append(7)
    list_one.afterInsert(3,list_one.head.next)
    list_one.printList()



