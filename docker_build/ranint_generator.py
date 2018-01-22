#!/usr/local/bin/python
import time
import sys
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


# Container will run for 1min. generate a custom 2 digit exit code between 1-42 and exit
# passing code back to the pod's Termination stderr log

time.sleep(60)

# Generating 2 digit exit Code and exiting...
code=random_with_N_digits(2)
sys.exit(code)
