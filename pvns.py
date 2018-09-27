"""
Script to assist with picking from PVNS values
"""

import math


PVNS_5 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 24, 27, 30, 33, 36, 39,
          43, 47, 51, 56, 62, 68, 75, 82, 91]

# Gets closest pvns pair for ratio = n/d
# Assumes 0 < ratio < 1
# Returns list of tuples of PVNS values (n, d, error)
# in order of descending error
def get_closest_pvns(ratio, pvns, pairs_to_return=3):
    closest_n = pvns[0]
    closest_d = pvns[0]
    closest_error = abs(ratio - closest_n / closest_d)
    closest_values = [(closest_n, closest_d, closest_error)] * pairs_to_return
    mag_diff = abs(math.floor(math.log(ratio, 10)))
    denominators = [
        x * pow(10, exponent)
        for exponent in range(mag_diff + 1)
        for x in pvns]

    # Check all pvns values until smallest error is found
    for n in pvns:
        for d in denominators:
            error = abs(ratio - n / d)
            if error < closest_error:
                closest_n = n
                closest_d = d
                closest_error = error
                closest_values.insert(0, (closest_n, closest_d, closest_error))
                closest_values.pop()
    return closest_values

if __name__ == '__main__':
    print(get_closest_pvns(0.5, PVNS_5, 5))
