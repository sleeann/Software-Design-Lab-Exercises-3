
# Structure of a Tree Node


class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Function to get the left height of
# the binary tree
def left_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.left

    # Return the left height obtained
    return ht


# Function to get the right height
# of the binary tree
def right_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.right

    # Return the right height obtained
    return ht


# Function to get the count of nodes
# in complete binary tree
def TotalNodes(root):
    # Base case
    if (root == None):
        return 0

    # Find the left height and the
    # right heights
    lh = left_height(root)
    rh = right_height(root)

    # If left and right heights are
    # equal return 2^height(1<<height) -1
    if (lh == rh):
        return (1 << lh) - 1

    # Otherwise, recursive call
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)


# Driver code
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)

print(TotalNodes(root))
