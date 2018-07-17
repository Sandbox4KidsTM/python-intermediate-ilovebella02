# -*- coding: utf-8 -*-


class My_Stack():
    def __init__(self):
        self._stack = []
        
    def _repr_(self):
        return" ", __join__(str(x) for x in self._stack.reverse())
        
    def push(self, item):
        self._stack.append(item)
        
    def pop(self):
        return self._stack.pop()
    
    def peek(self):
        return self._stack[-1]
    
stack = My_Stack()
stack.push("Red")
stack.push("Green")
stack.push("Blue")

stack.peek() == "Blue"
stack.pop() == "Blue"
print(stack)
        