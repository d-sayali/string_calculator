import re
import numpy as np

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = [",", "\n"]
        
        custom_delimiter_pattern = r"^//(\[.*?\]|\S)\n"

        # Check for custom delimiter
        match = re.match(custom_delimiter_pattern, numbers)
        
        if match:
            delimiter_section = match.group(1)
            numbers = numbers[len(match.group(0)):]  # Remove delimiter section from input

            # Extract multiple/multi-char delimiters
            delimiters = re.findall(r"\[([^]]+)]", delimiter_section) or [delimiter_section]

        # Use regex to split the numbers
        num_array = np.array(re.split("|".join(map(re.escape, delimiters)), numbers), dtype=np.int32)

        # Raise exception if there are negative numbers
        if (negatives := num_array[num_array < 0]).size > 0:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        
        # Add numbers, ignoring those greater than 1000
        return np.sum(num_array[num_array <= 1000])
