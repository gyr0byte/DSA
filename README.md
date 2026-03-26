# DSA in Python

A collection of Data Structures and Algorithms (DSA) programs written in Python and i don't know i might write sometimes in C cuz i love it.

## Current Contents

- `LinearSearch/`
  - `linear_search.py` - Linear Search implementation in Python.
  - `linear_searchh.c` - Linear Search implementation in C.
  - `linear_searchh.exe` - Compiled executable generated from the C file.

## About Linear Search

Linear Search checks each element in a list one by one until:

1. The target is found, or
2. The list ends.

### Time Complexity

- Best Case: `O(1)` (target found at first position)
- Average Case: `O(n)`
- Worst Case: `O(n)` (target at last position or not present)

### Space Complexity

- `O(1)` (constant extra space)

## Getting Started

### Prerequisites

- Python 3.x installed

### Run the Program

From the project root:

```bash
python LinearSearch/linear_search.py
```

Or on Windows:

```bash
python -u "c:\Users\MSI\Desktop\Python\DSA\LinearSearch\linear_search.py"
```

## Folder Structure

```text
DSA/
└── LinearSearch/
  ├── linear_search.py
  ├── linear_searchh.c
  └── linear_searchh.exe
```

## Learning Goals

- Understand how searching works in unsorted data.
- Compare Linear Search with faster methods like Binary Search.
- Practice writing clean, beginner-friendly Python code.

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Add your algorithm or improvements
4. Submit a pull request

## License

This project is for educational purpose.
