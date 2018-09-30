# CircuitsHelpers
Some helper scripts for circuits

# pvns.py
Finds n closest PVNS pairs to create specified ratio
Ratio must be between 0 and 1
Usage: `python pvns.py <r1/r2 ratio> <number of results to display>`

# schmitt.py
Calculates min/max hysterisis voltage and resistor values for
inverting Schmitt trigger circuit
Usage: `python schmitt.py <r1> <r2> <r3> <tolerance> <v_ref>`
Where r1, r2, r3 are nominal resistor values specified tolerance