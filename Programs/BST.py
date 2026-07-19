class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self._insert(self.root, item)

    def _insert(self, node, item):
        if item < node.item:
            if node.left is None:
                node.left = Node(item)
            else:
                self._insert(node.left, item)
        else:
            if node.right is None:
                node.right = Node(item)
            else:
                self._insert(node.right, item)

    def delete(self, item):
        self.root = self._delete(self.root, item)
        
    def _delete(self, node, item):
        if node is None:
            return node  # Node not found
        
        # If the item to be deleted is smaller than the node's item, go left
        if item < node.item:
            node.left = self._delete(node.left, item)
        
        # If the item to be deleted is larger than the node's item, go right
        elif item > node.item:
            node.right = self._delete(node.right, item)
        
        # Node to be deleted is found
        else:
            # Case 1: Node has no children (leaf node)
            if node.left is None and node.right is None:
                return None  # Simply remove the node
            
            # Case 2: Node has one child
            elif node.left is None:
                return node.right  # Replace node with its right child
            elif node.right is None:
                return node.left  # Replace node with its left child
            
            # Case 3: Node has two children
            else:
                # Get the in-order successor (smallest node in the right subtree)
                temp = self._min_value_node(node.right)
                node.item = temp.item  # Replace current node's item with successor's item
                node.right = self._delete(node.right, temp.item)  # Delete successor node

        return node

    def _min_value_node(self, node):
        current = node
        # Loop down to find the leftmost leaf (smallest item)
        while current.left is not None:
            current = current.left
        return current

    def display(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.item, end=" ")
            self._inorder_traversal(node.right)

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