class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:
    def __init__(self):
        self.head=None

    def ins_first(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            self.head=new_node
        print("Node inserted successfully!!")

    def ins_last(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
        print("Node inserted successfully!!")

    def del_first(self):
        if self.head==None:
            print("List is empty")
            return
        if self.head.next==self.head:
            print(self.head.data,"deleted successfully")
            self.head=None
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=self.head.next
        self.head=self.head.next
        print("Node deleted successfully")


    def del_last(self):
        if self.head==None:
            print("List is empty")
            return
        if self.head.next==self.head:
            print(self.head.data,"deleted successfully")
            self.head=None
            return
        temp=self.head
        while temp.next.next!=self.head:
            temp=temp.next
        temp.next=self.head
        print("Node deleted successfully")

    def display(self):
        if self.head==None:
            print('List is empty!!')
            return
        temp=self.head
        while True:
            print(temp.data,end='-->')
            temp=temp.next
            if temp==self.head:
                break
        print("(head)")

def main():
    ll1=CLL()
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