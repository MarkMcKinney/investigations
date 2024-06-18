# This is my first take at a Python impementation for the algorithm introduced here: https://arxiv.org/pdf/2301.10191
# The algorithm estimates the amount of distinct elements in a stream. I measure the time it takes finish estimating as well.

import math
import random
import datetime

# Creating test stream
def create_test_stream(start=1, end=1000000, repeats=792):
    # Create a list of unique numbers
    unique_numbers = list(range(start, (end - repeats)))
    # Randomly select X numbers to repeat
    repeated_numbers = random.sample(unique_numbers, repeats)
    # Create the final list of X numbers
    numbers = unique_numbers + repeated_numbers
    # Shuffle the list to mix the unique and repeated numbers
    random.shuffle(numbers)
    return {"stream": numbers, "correct_uniques": end - repeats}

# Algo variables
stream_obj = create_test_stream()
stream = stream_obj["stream"]
p = 1  # sampling probability
X = set()  # will store a subset of elements from stream
# estimation is within this percentage's estimate (within 10%)
error_tolerance = 0.2
failure_probability = 0.01  # your confidence level — 99% confidence = 0.01
m = len(stream)

# You can calculate thresh below as mentioned in the paper...
# thresh = math.ceil((12 / error_tolerance**2) * math.log(8 * m / failure_probability)) # controls the size of X
# Or you can create a more static value...
thresh = math.ceil(0.01 * m)

# Start time
timestart = datetime.datetime.now()

# Algo in action
for item in stream:
    # if item is already in X, remove it to ensure that X only contains unique elements
    X.discard(item)
    # with prob p add item to X set
    if random.random() < p:
        X.add(item)
    if len(X) == thresh:
        X = {x for x in X if random.random() >= 0.5}
        p /= 2
        if len(X) == thresh:
            raise ValueError("Algorithm error!")

output = len(X) / p
# End time
timeend = datetime.datetime.now()

# Results
print("Threshold:", thresh)
print("Completed in:", timeend - timestart, "seconds")
print("Estimated distinct elements total:", output)
print("Actual distinct elements:", stream_obj["correct_uniques"])
print("Variance %:", 100 * (output -
      stream_obj["correct_uniques"])/stream_obj["correct_uniques"])
