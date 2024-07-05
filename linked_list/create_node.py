class student:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        node1 = student(data)
        if self.head == None:
            self.head = node1
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node1
            
    def print_list(self):
        if self.head == None:
            return
        else:
            temp = self.head
            while temp.next != None:
                print(temp.data)
                temp = temp.next
            print(temp.data)
        
list1 = linkedlist()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.print_list()
