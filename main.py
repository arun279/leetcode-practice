import os
from collections import Counter

def run_py_files(directory, except_file):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != except_file:
                if file != "main.py":
                    exec(open(os.path.join(root, file)).read())

if __name__ == "__main__":
    run_py_files(".", "generate_launch.py")