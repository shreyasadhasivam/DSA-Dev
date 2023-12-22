class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key

#In Order: visit left, root, right   
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" "),
        printInorder(root.right)
#Post Order: visit left, right then root
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=" ")

#Pre Order: visit root, left, then right
def printPreorder(root):
    if root:
        print(root.val, end= " ")
        printPreorder(root.left)
        printPreorder(root.right)


if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right= Node(5)

    print("Inorder traversal of BT is: ")
    printInorder(root)
    print("\nPostorder traversal of BT is: ")
    printPostorder(root)
    print("\nPreorder traversal of BT is: ")
    printPreorder(root)

