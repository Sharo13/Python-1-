class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def remove_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Original List:")
linked_list.display()

linked_list.remove_tail()

print("\nList after removing tail:")
linked_list.display()

# ///////////////////////////////////////////////////////////////////////////
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)



print("Top element of the stack:", stack.peek())
stack.pop()
print("Top element of the stack after 1 pop:", stack.peek())
stack.pop()
print("Top element of the stack after 2 pop:", stack.peek())
stack.pop()
print("Top element of the stack after 3 pop:", stack.peek())

