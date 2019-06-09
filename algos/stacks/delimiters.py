from stacks import StackArray

def delimiter_match(expression):
    """ Return True if an expressions contains correct pairings of delimiters. Return False otherwise"""
    open_delimiters = '({['  # opening delimiters
    close_delimiters = ')}]' # closing delimiters

    X = StackArray() # create StackArray instance
    for char in expression: #scan every character in the expression
        if char in open_delimiters: # if the character is an opening delimiter
            X.push(char) # push it on the stack
        elif char in close_delimiters: # if the character is a closing delimiter
            if X.is_empty():
                return False # no match found
            if close_delimiters.index(char) != open_delimiters.index(X.pop()):
                return False # mismatch found
    return X.is_empty() # are all symbols matched?

print(delimiter_match('[(7 + x) - (y + z)]'))


'''
We perform a left-to-right scan of the expression.
Each time we find an opening symbol which is one of the three symbols in the set '({[', we push it on the stack.
Each time we find a closing symbol, we pop a symbol from the stack and compare these two symbols for valid pairing.If we reach the 
end of the expression and the stack is empty then the original expression was properly matched.


'''


