def fibonacci_recursive(n):
    """Return the nth Fibonacci number using direct recursion."""
    # Validate the required integer input before starting recursion.
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be nonnegative.")

    # Base cases stop the recursion.
    if n <= 1:
        return n

    # Brute-force recursion recalculates the same smaller Fibonacci
    # values many times, which causes exponential growth in work.
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dynamic(n):
    """Return the nth Fibonacci number using bottom-up dynamic programming."""
    # Validate the required integer input.
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be nonnegative.")

    if n <= 1:
        return n

    # Store intermediate Fibonacci values so each value is computed once.
    fibonacci_values = [0, 1]

    # Build the sequence from the two known base values up through F(n).
    for index in range(2, n + 1):
        next_value = fibonacci_values[index - 1] + fibonacci_values[index - 2]
        fibonacci_values.append(next_value)

    return fibonacci_values[n]

import time

test_values = [5, 10, 20, 30, 35]
timing_results = []

for n in test_values:
    recursive_start = time.perf_counter()
    recursive_result = fibonacci_recursive(n)
    recursive_time = time.perf_counter() - recursive_start

    dynamic_start = time.perf_counter()
    dynamic_result = fibonacci_dynamic(n)
    dynamic_time = time.perf_counter() - dynamic_start

    # Both implementations must return the same Fibonacci number.
    assert recursive_result == dynamic_result

    timing_results.append((n, recursive_time, dynamic_time))

print(f"{'n':>5} | {'Recursive (s)':>15} | {'Dynamic (s)':>15}")
print("-" * 43)

for n, recursive_time, dynamic_time in timing_results:
    print(f"{n:>5} | {recursive_time:>15.8f} | {dynamic_time:>15.8f}")

import sys

recursion_limit = sys.getrecursionlimit()
failure_test_n = recursion_limit + 10

print("Python recursion limit:", recursion_limit)
print("Failure-test n:", failure_test_n)

recursive_completed = True

try:
    fibonacci_recursive(failure_test_n)
except RecursionError as error:
    recursive_completed = False
    print("Recursive function failed first:", type(error).__name__)

dynamic_start = time.perf_counter()
dynamic_result = fibonacci_dynamic(failure_test_n)
dynamic_time = time.perf_counter() - dynamic_start

print("Recursive function completed:", recursive_completed)
print("Dynamic-programming function completed:", True)
print("Dynamic-programming execution time (seconds):", f"{dynamic_time:.8f}")
print("Digits in F(n):", len(str(dynamic_result)))
