# Problem Description:
# Given a stream of elements too large to store in memory,
#  pick a random element from the stream with uniform probability.

import unittest
import random


# Assumptions for this problem:
#   For ease of implementation, the stream will be represented as an array
#   that we iterate through.
def random_element(stream):

    current = (0, 0)
    for el in stream:
        rand_val = random.random()
        if rand_val > current[1]:
            current = (el, rand_val)
    return current[0]

# A Standard Test Case does not seem to be ideal, so we'll check the uniformity of the
#   random distribution instead


if __name__ == "__main__":
    n = 100
    count = [0] * n
    stream = [x for x in range(n)]
    for i in range(n * 1000):
        count[random_element(stream)] += 1

    print(count)
