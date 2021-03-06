from singly_linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# With Array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         self.storage.pop()
    
# With doubly linked list
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)

#     def pop(self):
#         if self.size != 0:
#             self.size -= 1
#             return self.storage.remove_from_tail()
#         else:
#             return None

# with singly linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_end(value)

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None