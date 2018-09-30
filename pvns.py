"""
Script to assist with picking from 5% PVNS values
Usage: `python pvns.py <r1/r2 ratio> <number of results to display>`
Ratio must be between 0 and 1
"""

import math
import sys


PVNS_5 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 24, 27, 30, 33, 36, 39,
          43, 47, 51, 56, 62, 68, 75, 82, 91]

# Gets closest pvns pair for ratio = n/d
# Assumes 0 < ratio < 1
# Returns list of tuples of PVNS values (n, d, error)
# in order of descending error
def get_closest_pvns(ratio, pvns, pairs_to_return=3):
    closest_error = abs(ratio - 1)
    closest_values = [(pvns[0], pvns[0], closest_error)] * pairs_to_return
    mag_diff = abs(math.floor(math.log(ratio, 10)))
    denominators = [
        x * pow(10, exponent)
        for exponent in range(mag_diff + 1)
        for x in pvns]

    # Check all pvns values until smallest error is found
    for n in pvns:
        for d in denominators:
            error = abs(ratio - n / d)
            for i in range(len(closest_values)):
                if error < closest_values[i][2]:
                    closest_values.insert(i, (n, d, error))
                    closest_values.pop()
                    break
    return closest_values

if __name__ == '__main__':
    # Read arguments
    if len(sys.argv) < 3:
        sys.exit(-1)
    ratio = float(sys.argv[1])
    n = int(sys.argv[2])

    # Validate input
    if ratio <= 0 or ratio >= 1:
        print('Input ratio not between 0 and 1')
        sys.exit(1)

    # Calculate closest PVNS and display output
    for values in get_closest_pvns(ratio, PVNS_5, n):
        print('R1\t', values[0])
        print('R2\t', values[1])
        print('Error\t', values[2])
        print()
