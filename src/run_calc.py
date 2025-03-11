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
    ]


    # Run test case and print the output
    for test_input in inputs:
        result = StringCalculator.add(test_input)
        print(f"Input: {repr(test_input)} => Output: {result}")


if __name__ == "__main__":
    main()
