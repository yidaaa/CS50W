import unittest
from functions import is_prime

# unit test is a library, can test for both front end and back end functions
# assert fuctions include: assertEqual/NotEqual, assertTrue/False, assertIn/NotIn

class Tests(unittest.TestCase):

    def test_1(self):
        # check 1 is not prime
        self.assertFalse(is_prime(1))

    def test_2(self):
        # check 2 is prime
        self.assertTrue(is_prime(2))
    
    def test_8(self):
        # check 5 is prime
        self.assertFalse(is_prime(8))

    def test_11(self):
        # check 11 is prime
        self.assertTrue(is_prime(11))
    
    def test_25(self):
        # check 25 is not prime
        self.assertFalse(is_prime(25))
    
    def test_28(self):
        # check 1 is not prime
        self.assertFalse(is_prime(28))
    
if __name__ == "__main__":
    unittest.main()

    