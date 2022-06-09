class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def lengthOfLinkedList(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count 

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next    

        itr.next = Node(data, None)

    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)    

    def insertAtIndex(self, index, data):
        if index<0 or index>self.lengthOfLinkedList():
            raise Exception("Invalid index")
        if index == 0:
            self.insertAtBeginning(data)
            return 
        itr = self.head
        count = 1                      
        while(count != index):
            count+=1
            itr = itr.next
        node = Node(data, itr.next)
        itr.next = node

    def removeAtIndex(self, index):
        if index<0 or index>=self.lengthOfLinkedList():
            raise Exception("Invalid index")
        if index==0:
            self.head = self.head.next 
            return
              
        itr = self.head
        count = 1
        while count != index:           
            count+=1
            itr = itr.next
            
        itr.next = itr.next.next  

    def printL(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        itr = self.head
        llstr = ''
        while itr:
            x = lambda itr: '-->' if(itr.next) else ''
            llstr += str(itr.data) + str(x(itr))
            itr = itr.next    
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertValues(["banana", 'mango', 'grapes', 'orange'])
    ll.insertAtBeginning(5)
    ll.insertAtBeginning(59)
    ll.insertAtEnd(678)
    ll.removeAtIndex(1)
    ll.insertAtIndex(3, 'dev')
    ll.printL()
    print('Length of the LL = ', ll.lengthOfLinkedList())