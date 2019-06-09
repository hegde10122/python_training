from emptyerr import EmptyError

class StackArray:
    """ LIFO stack implementation using a Python list"""
    
    def __init__(self):
        """ create an empty stack"""
        self._stack = [] #non public stack instance initially empty

    def __len__(self):
        """ Return the number of elements in the stack"""
        return len(self._stack)

    def is_empty(self):
        """ Return True if the stack has no elements"""    
        return self.__len__() == 0

    def push(self,elem):
        """ Add element to the top of the stack"""
        self._stack.append(elem) # new element stored at the end of the stack

    def peek(self):
        """ Return the element at the top of the stack without removing it
            Raise empty error exception if stack has no elements
        """
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._stack[-1]  # the last item in the stack

    def pop(self):
        """ Remove the element from the top of the stack and return the same (LIFO operation)
            Raise empty error exception if stack has no elements
        """
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._stack.pop() # remove element t index -1 or the last item
    
    


