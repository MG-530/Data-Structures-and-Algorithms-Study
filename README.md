# Data Structures and Algorithms Study

This repository contains implementations of various data structures and algorithms problems. The implementations are designed for educational purposes and include detailed visualizations and explanations.

## Current Implementations

### 1. Polynomial Operations Using Linked Lists
A comprehensive implementation of polynomial operations using linked list data structure.

#### Features
- Create polynomials from string input
- Add/multiply polynomials
- Calculate derivatives and integrals
- Sorted term insertion
- String representation

#### Time Complexity
- Addition: O(n + m)
- Multiplication: O(n * m)
- Differentiation: O(n)
- Integration: O(n)

### 2. Knight's Tour Using Backtracking
An interactive visualization of the Knight's Tour problem using Python's Turtle graphics.

#### Features
- Interactive chessboard visualization
- Warnsdorff's algorithm implementation
- Visual representation of moves
- Path tracking with numbered moves
- Connected path visualization

#### Time Complexity
- Space Complexity: O(N²) for the visited array
- Time Complexity: O(N²) with Warnsdorff's heuristic

## Usage

### Polynomial Operations
```python
# Create polynomial objects
poly1 = Polynomial()
poly2 = Polynomial()

# Create from strings
poly1.create_from_string_sorted("3x^2 + 2x^1 + 5")
poly2.create_from_string_sorted("1x^5 + 3x^2 + 3")

# Perform operations
sum_poly = poly1.add_polynomials(poly2)
product_poly = poly1.multiply_polynomials(poly2)
```

### Knight's Tour
```python
# Run the program
python chess.py

# Enter starting position when prompted
Enter the starting column (1-8): 1
Enter the starting row (1-8): 1
```

## Requirements
- Python 3.x
- turtle (built-in module)

## Project Structure
```
data-structures-study/
├── polynomial_by_listnode.py
├── chess.py
└── README.md
```

## Implementation Details

### Polynomial Implementation
- Uses a linked list to store terms
- Each node contains coefficient and exponent
- Maintains terms in descending order of exponents
- Supports string parsing for easy input

### Knight's Tour Implementation
- Uses Warnsdorff's algorithm for move selection
- Visual representation using Turtle graphics
- Interactive chessboard with move numbers
- Path visualization with connected lines
- Input validation for board boundaries

