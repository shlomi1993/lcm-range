# Shlomi Ben-Shushan
import sys
import time

# Start timer.
start_time = time.time()

# Compute GCD with euclidean algorithm.
def compute_gcd(x, y):
    while (x != 0 and y != 0):
        if x > y:
            x = x % y
        elif x < y:
            y = y % x
        else:
            return x
    if x == 0:
        return y
    else:
        return x

# Compute LCM with LCM formula.
def compute_lcm(x, y):
    return abs(x * y) // compute_gcd(x, y)

# Compute LCM of range with multiple-LCM formula.
def compute_lcm_range(start, end):
    rng = range(start, end + 1)
    lcm = compute_lcm(1, 2)
    for i in range(2, len(rng)):
        lcm = compute_lcm(lcm, rng[i])
    return lcm

# Gets input, compute range-LCM and print it's result and execution time.
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    assert(a > 0 and b > 0 and a <= b)
    print("LCM from %d to %d is %d." % (a, b, compute_lcm_range(a, b)))
    print("Execution time: %s seconds." % (time.time() - start_time))
except:
    print("Invalid input")
