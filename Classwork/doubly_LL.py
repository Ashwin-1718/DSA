class Node:
    def __init__(self,data):
        self.data=data
        self.forw=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None

    def ins_first(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            print("Node inserted successfully!!")
            return
        new_node.forw=self.head
        self.head.prev=new_node
        self.head=new_node
        print("Node inserted successfully!!")

    def ins_last(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            print("Node inserted successfully!!")
            return
        temp=self.head
        while temp.forw!=None:
            temp=temp.forw
        temp.forw=new_node
        new_node.prev=temp
        print("Node inserted successfully!!")

    def del_first(self):
       if self.head==None:
            print("List is empty!!")
            return 
       if self.head.forw==None:
           self.head=None
           print("Node deleted successfully!!")
           return
       self.head=self.head.forw
       self.head.prev=None
       print("Node deleted successfully!!")

    def del_last(self):
        if self.head==None:
            print("List is empty!!")
            return 
        if self.head.forw==None:
           self.head=None
           print("Node deleted successfully!!")
           return
        temp=self.head
        while temp.forw:
            temp=temp.forw
        temp.prev.forw=None
        print("Node deleted successfully!!")
    
    def display(self):
        if self.head==None:
            print("List is empty!!")
            return  
        temp=self.head
        while temp:
            print(temp.data,end="<-->")
            temp=temp.forw
        print("(None)")  
          
    def rev_display(self):
        if self.head==None:
            print("List is empty!!")
            return  
        temp=self.head
        while temp.forw!=None:
            temp=temp.forw
        current=temp
        while current:
            print(current.data,end="<-->")
            current=current.prev
        print("(None)")  

def main():
    ll1=DLL()
    while True:
        print("======Menu======")
        print("1) Insert at first")
        print("2) Insert at last")
        print("3) Delete first")
        print("4) Delete last")
        print("5) Display")
        print("6) Display Reverse")
        print("7) Exit")
       
        
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
                ll1.rev_display()
            case 7:
                return
            case _:
                print("Enter valid choice")
            
main()