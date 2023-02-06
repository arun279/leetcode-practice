# leetcode-practice

This repository contains solutions to LeetCode problems from [Grind 75](https://www.techinterviewhandbook.org/grind75), grouped by topics. Each solution file is named with the corresponding LeetCode problem number.

## Usage
- To test, use the following command:
```
python -m unittest discover -s tests
```
- You can also run individual test methods in `tests/test_all.py` using your IDE's testing framework.

## Questions Solved

### Arrays
1. [Two Sum](https://leetcode.com/problems/two-sum/)
20. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### Binary Tree
102. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
104. [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### Graph
133. [Clone Graph](https://leetcode.com/problems/clone-graph/)
200. [Number of Islands](https://leetcode.com/problems/number-of-islands/)

### Hash Table
41. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
380. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
383. [Ransom Note](https://leetcode.com/problems/ransom-note/)

### Heap
215. [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### Linked List
146. [LRU Cache](https://leetcode.com/problems/lru-cache/)
206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

### Matrix
36. [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

### Not in Grind 75
232. [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### Not in Leetcode 
1. [Seven Segment Display to String]()

## Contribute
If you would like to contribute, you can submit PRs with leetcode solutions from [Grind 75](https://www.techinterviewhandbook.org/grind75) that have not already been added, following these requirements:
- Keep the naming contention: filename starts with LeetCode question number, followed by the question.
- The docstring in the file should be a link to the the LeetCode problem.
- Update the README.md with the solved questions added.
- For every problem, add a corresponding test method to `tests/test_all.py`.

PRs that don't follow these requirements won't be merged.

## Note

`run_tests` has now been completely removed from `master`. Please checkout `legacy_run_tests` branch in order to use it.