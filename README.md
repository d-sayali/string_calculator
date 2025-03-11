# String Calculator

## Overview
String Calculator is a simple utility that performs basic arithmetic operations on numbers provided in a string format. It currently demonstrates addition operation with some combinations.

## Features
- Supports addition (`+`).
- Handles multiple numbers in a single string with custom delimiters for integer separation.
- Returns meaningful error messages for invalid inputs.

## Installation
To use the String Calculator, clone the repository and install the dependencies if applicable.

```sh
# Clone the repository
git clone https://github.com/d-sayali/string_calculator

# Change into the project directory
cd string-calculator
```

## Usage
To run the String Calculator, use the command line or integrate it into your application.

```python
from calculator import StringCalculator

result = StringCalculator.add("3,5,2,8,4")
print(result)  # Output: 22
```

## Running Tests
To run the test suite, use the following command:

```sh
pytest tests/
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
