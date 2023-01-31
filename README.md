# leetcode-practice

This repository contains solutions to LeetCode problems from [Grind 75](https://www.techinterviewhandbook.org/grind75), grouped by topics. Each solution file is named with the corresponding LeetCode problem number.

## Usage

- Testing individual files and using `run_tests` has been deprecated. The tests are now written in `tests/test_all.py` using `unittest`.
- To test, use the following command:
```
python -m unittest discover -s tests
```
- You can also run individual test methods in `tests/test_all.py` using your IDE's testing framework.

## Questions Solved so far

### Arrays
1. [Two Sum](https://leetcode.com/problems/two-sum/)
20. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### Hash Table
41. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
380. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
383. [Ransom Note](https://leetcode.com/problems/ransom-note/)

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

- You can submit PRs with leetcode solutions from [Grind 75](https://www.techinterviewhandbook.org/grind75) that have not already been added.
- Keep the naming contention: filename starts with LeetCode question number, followed by the question. The docstring in the file should be a link to the the LeetCode problem. Update the README.md with the solved questions added.
- Don't add any testing inside these files as `run_tests()` has been deprecated. Instead, add a method to `tests/test_all.py`. PRs without tests will not be accepted.