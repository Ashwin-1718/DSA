class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(self.root,data)
        
    def _insert(self,node,data):
        if data<node.data:
            if node.left is None:
                node.left=Node(data)
            else:
                self._insert(node.left,data)
        else:
            if node.right is None:
                node.right=Node(data)
            else:
                self._insert(node.right,data)

    def delete(self,data):
        if self.root==None:
            print("Tree is empty")
            return
        self._delete(self.root,data)

    def inorder_successor(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current
    
    def _delete(self,node,data):
        if node is None:
            return node
        if data<node.data:
            node.left=self._delete(node.left,data)
        elif data>node.data:
            node.right=self._delete(node.right,data)
        else:
            if node.left==None and node.right==None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp=self.inorder_successor(node.right)
                node.data=temp.data
                node.right=self._delete(node.right,temp.data)
        return node
    

    def display(self):
        if self.root is None:
            print("Tree is empty!!")
        else:
            self.inorder(self.root)
        

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

def main():
    bst = BST()
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the item to insert: "))
            bst.insert(item)
        elif choice == 2:
            item = int(input("Enter the item to delete: "))
            bst.delete(item)
        elif choice == 3:
            print("BST In-order Traversal:")
            bst.display()
            print()  # For a new line
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()