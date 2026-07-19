class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def ins_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def ins_last(self,data):
        new_node=Node(data)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
        else:
            self.head=new_node
    
    def ins_loc(self,data,pos):
        if pos==0:
            self.ins_first(data)
            return
        new_node=Node(data)
        temp=self.head
        index=0
        while temp is not None and index<pos-1:
            temp=temp.next
            index=index+1
        if temp is None:
            print("Invalid position")
            return        
        new_node.next=temp.next
        temp.next=new_node
        print("Node inserted successfully!!")

    def del_first(self):
        if not self.head:
            print("List is empty")
            return
        else:
            if self.head.next==None:
                self.head=None
            else:
                self.head=self.head.next

    def del_last(self):
        if not self.head:
            print("List is empty")
            return
        else:
            if self.head.next==None:
                self.head=None
            else:
                temp=self.head
                while temp.next.next:
                    temp=temp.next
                temp.next=None

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp=self.head
        while temp:
            print(temp.data,"--->",end="\t")
            temp=temp.next
        print("None")

    def count(self):
        ctr=0
        temp=self.head
        while temp:
            if int(temp.data)>100:
                ctr=ctr+1
            temp=temp.next
        print(ctr)

    def copy(self):
        original=ll1.head    
        while original:
            if int(original.data)>200:
                new_node=Node(original.data)
                if self.head:
                    temp=self.head
                    while temp.next:
                        temp=temp.next        
                    temp.next=new_node
                else:
                    self.head=new_node
            original=original.next
ll1=LinkedList()
new_list=LinkedList()
def main():
    
    
    while True:
        print("======Menu======")
        print("1) Insert at first")
        print("2) Insert at last")
        print("3) Delete first")
        print("4) Delete last")
        print("5) Display")
        print("6) Exit")
        print("7)Insert at a specific location")
        print("8)Count")
        print("9)Copy")
        print("10)Display Copy")
        
        choice=int(input(f'Enter your choice:\t'))

        match choice:
            case 1:
                data=input(f'Enter data:\t')
                ll1.ins_first(data)
            case 2:
                data=input(f'Enter data:\t')
                ll1.ins_last(data)
            case 3:
                ll1.del_first()
            case 4:
                ll1.del_last()
            case 5:
                ll1.display()
            case 6:
                return
            case 7:
                data=input(f'Enter data: ')
                pos=int(input(f'Enter position:'))
                ll1.ins_loc(data,pos)
            case 8:
                ll1.count()

            case 9:
                new_list.copy()
            case 10:
                new_list.display()
            case _:
                print("Enter valid choice")
            
main()
            