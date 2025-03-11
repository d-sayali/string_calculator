import re
import numpy as np

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = [",", "\n"]
        
        # Use regex to split the numbers
        num_array = np.array(re.split("|".join(map(re.escape, delimiters)), numbers), dtype=np.int32)

        # Add numbers
        return np.sum(num_array)
