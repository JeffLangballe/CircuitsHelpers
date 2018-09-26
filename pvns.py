"""
Script to assist with picking from PVNS values
"""

PVNS_5 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 24, 27, 30, 33, 36, 39,
          43, 47, 51, 56, 62, 68, 75, 82, 91]

# Gets closest pvns pair for val = n/d
# Assumes 0 < val < 1
# Returns tuple of PVNS values (n, d) representing closest pair to val
def get_closest_pvns(val, pvns):
    closest_n = pvns[0]
    closest_d = pvns[0]
    closest_error = abs(val - closest_n / closest_d)
    for n in pvns:
        for d in pvns:
            error = abs(val - n / d)
            if error < closest_error:
                closest_n = n
                closest_d = d
                closest_error = error
    return (closest_n, closest_d)
    

if __name__ == '__main__':
    pair = get_closest_pvns(0.5, PVNS_5)
    print(pair)
