def run_tests(file_name, test_cases):
    print(f"Testing {file_name.__name__}:")
    for i, (inputs, expected_output) in enumerate(test_cases):
        try:
            result = file_name(*inputs)
            if result == expected_output:
                print(f"Test case {i + 1}: PASSED")
            else:
                print(f"Test case {i + 1}: FAILED")
                print(f"Inputs: {inputs}")
                print(f"Output: {result}")
                print(f"Expected Output: {expected_output}")
        except Exception as e:
            print(f"Test case {i + 1}: ERROR")
            print(f"Error: {e}")
