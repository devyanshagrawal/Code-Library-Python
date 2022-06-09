from matplotlib import collections


from collections import deque

# stack = deque()

# # print(dir(stack))  #show all methods present 

# stack.append('asdfghjk')
# print(stack)
# # print(stack.pop())
# # print(stack)
# print(stack.__len__())


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        if self.size() == 0:
            raise Exception('Empty Stack!')
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container) 

s = Stack()
s.push(78)
s.push(89)
print(s.size()) 
print(s.pop())
print(s.pop())
print(s.pop())          