import numpy as np
from scipy import stats

# Sample data array with equal occurrences of 1 and 0
data = np.array([1, 0, 1, 0, 0, 1])

# Find the mode
mode_result = stats.mode(data)

# Print the mode(s)
print("Mode:", mode_result.mode)
print("Count of the mode(s):", mode_result.count)