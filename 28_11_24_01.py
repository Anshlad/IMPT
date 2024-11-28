def is_balanced(parentheses):
    # Stack to keep track of opening parentheses
    stack = []
    
    # Dictionary to hold matching pairs
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in parentheses:
        # If the character is one of the closing parentheses
        if char in matching_parentheses:
            # Pop from stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else None
            
            # Check if the popped element matches the corresponding opening parenthesis
            if matching_parentheses[char] != top_element:
                return False
        # If it's an opening parenthesis, push onto the stack
        elif char in matching_parentheses.values():
            stack.append(char)
    
    # If the stack is empty, all parentheses were balanced
    return len(stack) == 0

# Example usage
input_string = "({[]})"
if is_balanced(input_string):
    print("The string of parentheses is balanced.")
else:
    print("The string of parentheses is not balanced.")