"""
Calculates min/max hysterisis voltage and resistor values for
inverting Schmitt trigger circuit
Usage: `python schmitt.py <r1> <r2> <r3> <tolerance> <v_ref>`
Where r1, r2, r3 are nominal resistor values specified tolerance
"""

import sys


def schmitt_v_lo(v_ref, r1, r2, r3):
    return v_ref / ((r2/r1) + (r2/r3) + 1)

def schmitt_v_hi(v_ref, r1, r2, r3):
    return v_ref / (1 + 1 / ((r1/r2) + (r1/r3)))

def get_extreme_schmitt_hysterisis(v_ref, resistances, tolerance):
    # Generate all resistor combinations with extreme tolerances
    resitance_min_max = [[r - r*tolerance, r+r*tolerance] for r in resistances]
    resistor_combinations = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resistors = [resitance_min_max[0][i],
                            resitance_min_max[1][j],
                            resitance_min_max[2][k]]
                resistor_combinations.append(resistors)
    
    # Find min/max hysterisis
    min_range = float('inf')
    max_range = float('-inf')
    for r in resistor_combinations:
        v_lo = schmitt_v_lo(v_ref, r[0], r[1], r[2])
        v_hi = schmitt_v_hi(v_ref, r[0], r[1], r[2])
        v_range = v_hi - v_lo
        if v_range < min_range:
            min_range = v_range
            min_params = (v_range, v_lo, v_hi, r)
        if v_range > max_range:
            max_range = v_range
            max_params = (v_range, v_lo, v_hi, r)
        # print(v_range, v_lo, v_hi, r)
    return(min_params, max_params)

if __name__ == '__main__':
    if len(sys.argv) < 6:
        sys.exit(-1)

    # Read input paraargumentsms
    resistances = [float(r) for r in sys.argv[1:4]]
    tolerance = float(sys.argv[4])
    v_ref = float(sys.argv[5])

    # Calculate voltages and resistor values
    params = get_extreme_schmitt_hysterisis(v_ref, resistances, tolerance)

    # Print output to console
    print('Minimum hysterisis values:')
    print('V range\t\t', params[0][0])
    print('V_tl\t\t', params[0][1])
    print('V_th\t\t', params[0][2])
    print('R1, R2, R3\t', params[0][3])

    print('\nMaximum hysterisis values:')
    print('V range\t\t', params[1][0])
    print('V_tl\t\t', params[1][1])
    print('V_th\t\t', params[1][2])
    print('R1, R2, R3\t', params[1][3])
