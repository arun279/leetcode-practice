# leetcode-practice

This repository contains solutions to LeetCode problems from [Grind 75](https://www.techinterviewhandbook.org/grind75), grouped by topics. Each solution file is named with the corresponding LeetCode problem number.

## Usage

1. To run individual solutions, you can just run the corresponding file. For example:
```
python array/1-two-sum.py
```

2. To test all the solutions in the repository, run the `main.py` file.
```
python main.py
```

3. Alternatively, you can utilize `generate_launch.py` if are using `vscode`. This helps generate a `launch.json` file which wiil helo you run the solutions through the "Run and Debug" function in vscode. To do this, create a `tasks.json` file in the `.vscode` folder. This file specifies the tasks that can be launched from the Command Palette. Here's an example of `tasks.json`
```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Generate launch.json",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}/generate_launch.py",
                "${workspaceFolder}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```
Once you do this, go to Command Palette (`ctrl + shift + p`) and click on "Tasks: Run Task". From there, select "Generate launch.json", this will create a `launch.json` inside `.vscode`. Now if you go to "Run and Debug" tab in vscode, you can run `main.py` or any individual file directly from there.


## Questions Solved so far

### Arrays
1. [Two Sum](https://leetcode.com/problems/two-sum/)
20. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### Hash Table
41. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
380. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
383. [Ransom Note](https://leetcode.com/problems/ransom-note/)

## Contribute

- You can submit PRs with leetcode solutions from [Grind 75](https://www.techinterviewhandbook.org/grind75) that have not already been added.
- Keep the naming contention: filename starts with LeetCode question number, followed by the question. The docstring in the file should be a link to the the LeetCode problem. Update the README.md with the solved questions added.
- In the file, use `run_tests()` from `run_tests.py` to test the solution, you have to pass the method name and a list of test cases, where each test case contains a tuple of input and expected output.