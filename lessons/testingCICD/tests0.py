from functions import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")

# you can test it this way
test_prime(5, True)
test_prime(8, False)
test_prime(25, False)
