from calculator import StringCalculator

def main():
    # Sample Input
    inputs = [
        "",                 # Empty input
    ]


    # Run test case and print the output
    for test_input in inputs:
        result = StringCalculator.add(test_input)
        print(f"Input: {repr(test_input)} => Output: {result}")


if __name__ == "__main__":
    main()
