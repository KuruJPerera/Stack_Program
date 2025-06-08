
# Stack Implementation in Python

This project demonstrates a basic stack data structure implemented using Python's built-in `list` type. A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle—meaning the last item added is the first one removed.

---

## What is a Stack?

A stack is like a pile of plates — you add to the top, and remove from the top. It supports two main operations:

- **Push**: Add an item to the top of the stack
- **Pop**: Remove and return the top item from the stack

Stacks are commonly used in programming for undo mechanisms, parsing expressions, and tracking function calls.

---

## How It Works

The script includes two main functions:

- `push(stack, item)`: Adds `item` to the top of the stack
- `pop(stack)`: Removes and returns the top item. Returns `None` if the stack is empty.

The stack itself is represented by a standard Python list.

---

## Example Usage

```python
stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)

print("Stack after pushes:", stack)
# Output: Stack after pushes: [10, 20, 30]

print("Popped:", pop(stack))
# Output: Popped: 30

print("Stack after pop:", stack)
# Output: Stack after pop: [10, 20]
```

---

## Getting Started

### Requirements

- Python 3

This script requires no external packages. It runs entirely with built-in Python functionality.

---

## Running the Program

1. Save the code to a file (e.g., `stack.py`)  
2. Run it using:
   ```bash
   python stack.py
   ```

You’ll see how items are added and removed from the stack.

---
