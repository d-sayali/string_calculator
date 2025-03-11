import re
import numpy as np

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if not numbers:
            return 0

        # split string into numpy array
        num_array = np.array(re.split(",", numbers), dtype=np.int32)

        # Add numbers
        return np.sum(num_array)
