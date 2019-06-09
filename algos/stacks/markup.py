from stacks import StackArray

'''
<body><center><h1>The Boat</h1></center><p>Lorfsffaf</p><ol><li>123</li><li>456</li><li>789</li><li>ABC</li></ol></body>
'''

def match_html(input_text):
    """ Return True if all HTML tags are properly matched, False otherwise"""
    X = StackArray()
    index = input_text.find('<') # find first '<' character (if any)
    while index != -1:
        next_tag = input_text.find('>', index+1) # find next '>' character
        if next_tag == -1:
            return False # invalid tag
        tag = input_text[index+1:next_tag] #strip away < >
        if not tag.startswith('/'): # this is opening tag
            X.push(tag)
        else: # this is closing tag
            if X.is_empty():
                return False  # nothing to match with
            if tag[1:]!=X.pop():
                return False # mismatched delimiter
        index = input_text.find('<',next_tag+1) # find next '<' character if any
    return X.is_empty() # were all opening tags matched?

print(match_html('<h1></h1>'))



 