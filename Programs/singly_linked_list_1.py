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
        
def main():
    ll1=LinkedList()
    while True:
        print("======Menu======")
        print("1) Insert at first")
        print("2) Insert at last")
        print("3) Delete first")
        print("4) Delete last")
        print("5) Display")
        print("6) Exit")
        
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
            case _:
                print("Enter valid choice")
            
main()