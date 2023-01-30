import os
import sys
import traceback
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from collections import Counter

def run_py_files(directory, except_files):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file not in except_files:
                print(f"Running file: {file}")
                try:
                    exec(open(os.path.join(root, file)).read())
                except Exception as e:
                    print(f"Error running file {file}: {e}")
                    print("Traceback:")
                    print("".join(traceback.format_tb(e.__traceback__)))

if __name__ == "__main__":
    run_py_files(".", ["generate_launch.py", "main.py"])