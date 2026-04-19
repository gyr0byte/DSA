# DSA in Python

A collection of Data Structures and Algorithms (DSA) programs written in Python and i don't know i might write sometimes in C cuz i love it.

## Current Contents

- `LinearSearch/`
  - `linear_search.py` - Linear Search implementation in Python.
  - `linear_searchh.c` - Linear Search implementation in C.
- `BinarySearch/`
  - `bn_search.py` - Binary Search implementation in Python.
  - `bn_search.c` - Binary Search implementation in C.
  - `first_last_index_arr.c` - Find first and last index of element in sorted array (C).
  - `first_last_index_arr.py` - Find first and last index of element in sorted array.
  - `right_or_left_minimum.py` - Find right or left minimum in rotated sorted array.
- `BinaryTree/`
  - `binary_tree.py` - Binary Tree implementation in Python.
  - `binary_tree_tuple.py` - Binary Tree using tuples in Python.
  - `height_of_tree.py` - Find the height of a binary tree.
  - `max_depth.py` - Find the maximum depth of a binary tree.
  - `min_depth.py` - Find the minimum depth of a binary tree.
  - `nmbr_of_nodes.py` - Count number of nodes in a binary tree.
- `BinarySearchTrees/`
  - `display.py` - Display Binary Search Tree values.
  - `is_balanced.py` - Check if a Binary Search Tree is balanced.
  - `key_value_pairs_bst.py` - Binary Search Tree with key-value pairs.
  - `maximum_key.py` - Find maximum key in a Binary Search Tree.
  - `minimum_key.py` - Find minimum key in a Binary Search Tree.
  - `str_bst.py` - Binary Search Tree with string values.
  - `validate_bst.py` - Validate whether a tree is a Binary Search Tree.
- `RotationCount/`
  - `rotation_count_linear.py` - Rotation count in a rotated sorted array (Python, linear approach).
  - `rotation_count_linear.c` - Rotation count in a rotated sorted array (C, linear approach).
- `TwoPointers/`
  - `move_zeros.py` - Move all zeros to the end using two pointers.
- `HashTables/`
  - `basic_hash_table.py` - Basic hash table implementation.
  - `handling_collsion_hash.py` - Handle collisions in hash tables.
  - `hashing_function.py` - Basic hashing function to compute index.
  - `improved_hash_table.py` - Improved hash table with better collision handling.
  - `insert.py` - Insert key-value data into hash table structure.
  - `list_kv.py` - List-based key-value storage example.
- `BubbleSort/`
  - `bubble_sort.py` - Bubble Sort implementation in Python.
- `InsertionSort/`
  - `insertion_sort.py` - Insertion Sort implementation in Python.
- `MergeSort/`
  - `merge_sort.py` - Merge Sort implementation in Python.
- `QuickSort/`
  - `quick_sort.py` - Quick Sort implementation in Python.
- `CustomComparisionFunc/`
  - `notebook_decreasing.py` - Custom comparison function example for sorting in decreasing order.
- `DynanicProgramming/`
  - `largest_common_subsequence.py` - Longest common subsequence implementation.
  - `lcs_with_memo.py` - Longest common subsequence using memoization.

## Getting Started

### Prerequisites

- Python 3.x installed
- GCC compiler installed (for running the C file)

### Run the Program

Run one Python file from the project root:

```bash
python LinearSearch/linear_search.py
```

### Compile and Run C File

Compile and run one C file from the project root:

```bash
gcc LinearSearch/linear_searchh.c -o LinearSearch/linear_searchh
./LinearSearch/linear_searchh
```

## Folder Structure

```text
DSA/
├── BinarySearch/
│   ├── bn_search.c
│   ├── bn_search.py
│   ├── first_last_index_arr.c
│   ├── first_last_index_arr.py
│   └── right_or_left_minimum.py
├── BinarySearchTrees/
│   ├── display.py
│   ├── is_balanced.py
│   ├── key_value_pairs_bst.py
│   ├── maximum_key.py
│   ├── minimum_key.py
│   ├── str_bst.py
│   └── validate_bst.py
├── BinaryTree/
│   ├── binary_tree.py
│   ├── binary_tree_tuple.py
│   ├── height_of_tree.py
│   ├── max_depth.py
│   ├── min_depth.py
│   └── nmbr_of_nodes.py
├── BubbleSort/
│   └── bubble_sort.py
├── HashTables/
│   ├── basic_hash_table.py
│   ├── handling_collsion_hash.py
│   ├── hashing_function.py
│   ├── improved_hash_table.py
│   ├── insert.py
│   └── list_kv.py
├── InsertionSort/
│   └── insertion_sort.py
├── MergeSort/
│   └── merge_sort.py
├── QuickSort/
│   └── quick_sort.py
├── CustomComparisionFunc/
│   └── notebook_decreasing.py
├── DynanicProgramming/
│   ├── largest_common_subsequence.py
│   └── lcs_with_memo.py
├── LinearSearch/
│   ├── linear_search.py
│   └── linear_searchh.c
├── RotationCount/
│   ├── rotation_count_linear.py
│   └── rotation_count_linear.c
└── TwoPointers/
    └── move_zeros.py
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
