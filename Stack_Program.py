# Stack.

# Stack implementation using a list

def push(stack, item):
    """Adds an item to the stack."""
    stack.append(item)

def pop(stack):
    """Removes and returns the top item from the stack."""
    if not stack:
        return None  # Stack is empty
    return stack.pop()

# Example usage
stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
print("Stack after pushes:", stack)
print("Popped:", pop(stack))
print("Stack after pop:", stack)
