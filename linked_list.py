class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
        
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
    def get(self, index):
        if index>=self.length():
            print("Index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx+=1
            
    def erase(self, index):
        if index>=self.length():
            print("Index out of range")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx+=1
        
my_list = linked_list()

my_list.append(1)

my_list.erase(2)
        
l1 = linked_list()
l1.append(2)
l1.append(4)
l1.append(3)

l2 = linked_list()
l2.append(5)
l2.append(6)
l2.append(4)
