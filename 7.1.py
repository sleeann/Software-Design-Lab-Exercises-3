#Creating Node
class Node:
    def _init_(self,x):
        self.val = x
        self.next = None

#Function to insert new node at front
def push(head, n_val):
    t = Node(n_val)
    t.next = head
    head = t
    return head

#Creating LL
head = None
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)
head = push(head, 4)
head = push(head, 5)

# 5 -> 4 -> 3 -> 2 -> 1 -> None

#Algorithm
temp = head
#check if list is empty
if (temp == None or temp.next == None):
    print("List is empty")

while (temp != None):
    if (temp.next.next == None):
        print(temp.val)
        break
    temp = temp.next
