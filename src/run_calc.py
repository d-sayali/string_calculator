from calculator import StringCalculator

def main():
    # Sample Input
    inputs = [
        "",                 # Empty input
        "1",                # Single number
        "1,5",              # Two numbers
        "1,2,3,4,5",        # Multiple numbers
        "1\n2,3",           # Newline as delimiter
        "//;\n1;2",         # Custom single-character delimiter
        "//[***]\n1***2***3",  # Custom multi-character delimiter
        "//[*][%]\n1*2%3",  # Multiple custom delimiters
        "//[***][%%%]\n1***2%%%3",  # Multiple custom multi-length delimiters
        "2,1001",           # Numbers greater than 1000 ignored
    ]


    # Run each test case and print the output
    for test_input in inputs:
        try:
            result = StringCalculator.add(test_input)
            print(f"Input: {repr(test_input)} => Output: {result}")
        except ValueError as e:
            print(f"Input: {repr(test_input)} => Exception: {e}")


    # Example case that raises an exception for negative numbers
    try:
        print(StringCalculator.add("1,-2,3,-5"))
    except ValueError as e:
        print(f"Negative Number Case: {e}")


if __name__ == "__main__":
    main()
