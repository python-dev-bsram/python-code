import warnings
import time
import tracemalloc

# 1. Prime number generator (for normal run and interactive example)
def generate_primes(n):
    """
      Generate prime numbers up to n.
    """
    primes = []
    for num in range(2, n + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if is_prime:
            primes.append(num)
    print("Prime numbers:", primes)
    return primes


# 2. Function with assertion (to test -O and -OO)
def check_positive(n):
    assert n > 0, "n must be positive"
    print(f"{n} is a positive number")


# 3. Function with warning (to test -W ignore and -W error)
def warning_test():
    warnings.warn("This is a test warning")


# 4. Function with time delay (to test unbuffered mode -u)
def delayed_print():
    for i in range(5):
        print(f"Delayed Count: {i}")
        time.sleep(1)


# 5. Function to profile (to test -m cProfile)
def slow_function():
    sum(range(10**6))


# 6. Function with memory allocation (to test -X tracemalloc)
def allocate_memory():
    return [i for i in range(10**6)]


# 7. Function to test isolated mode (-I)
def test_isolated_mode():
    try:
        import some_nonexistent_package  # Non-existent package
    except ImportError:
        print("Running in isolated mode: ImportError caught!")


# 8. Function to cause a crash (to test -X faulthandler)
def crash_function():
    return 1 / 0  # This will cause a ZeroDivisionError


if __name__ == "__main__":
    # 1. Generate prime numbers
    print("Generating Prime Numbers:")
    generate_primes(20)

    # 2. Check positive number (test -O and -OO optimizations)
    print("\nChecking Positive Number:")
    check_positive(10)

    # 3. Warning test (test -W ignore and -W error)
    print("\nRunning Warning Test:")
    warning_test()

    # 4. Delayed print (test unbuffered mode -u)
    print("\nRunning Delayed Print:")
    delayed_print()

    # 5. Slow function (test cProfile)
    print("\nRunning Slow Function:")
    slow_function()

    # 6. Memory allocation (test tracemalloc)
    print("\nRunning Memory Allocation:")
    tracemalloc.start()
    allocate_memory()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("\nTop memory allocations:")
    for stat in top_stats[:5]:
        print(stat)

    # 7. Test isolated mode
    print("\nTesting Isolated Mode:")
    test_isolated_mode()

    # 8. Crash function (test faulthandler)
    print("\nRunning Crash Function (This will raise ZeroDivisionError):")
    try:
        crash_function()
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")
