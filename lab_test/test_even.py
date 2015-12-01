import unittest
import lib
import math

class LibTest(unittest.TestCase):

#test_even

	def test_even_positive(self):
		self.assertEqual(lib.even(2), True)
		self.assertEqual(lib.even(7), False)
		self.assertEqual(lib.even(734), True)
		self.assertEqual(lib.even(0), True)
		self.assertEqual(lib.even(101), True)
		
	def test_even_negative(self):
		self.assertEqual(lib.even(-72), True)
	def test_even_negative_one(self):	
		self.assertEqual(lib.even(-1), False)
		self.assertEqual(lib.even(-15), False)
		
#test_factorial

	def test_factorial_positive(self):
		self.assertEqual(lib.factorial(0), 1)
		self.assertEqual(lib.factorial(6), 720)
		self.assertEqual(lib.factorial(1), 1)
		
	def test_factorial_negative(self):
		self.assertEqual(lib.factorial(-7), 1)	
		
#test_palindrome

	def test_palindrome(self):
		self.assertEqual(lib.palindrome('1221'), True)
		self.assertEqual(lib.palindrome('12321'), True)
	def test_palindrome_one(self):	
		self.assertEqual(lib.palindrome('атата'), True)		

#test_prime

	def test_prime(self):
		self.assertEqual(lib.prime(7), True)
		self.assertEqual(lib.prime(1), False)	
	def test_prime_one(self):
		self.assertEqual(lib.prime(-12), False)		

#test_sin

	def test_sin(self):
		self.assertEqual(lib.sin(math.pi/2), 1)
		self.assertEqual(lib.sin(-math.pi/2), -1)
		self.assertEqual(lib.sin(math.pi/6), 0.5)

#test_sqrt

	def test_sqrt_non_negative_arg(self):
		self.assertEqual(lib.sqrt(9), 3)
		self.assertEqual(lib.sqrt(1), 1)
		self.assertEqual(lib.sqrt(0), 0)

	def test_sqrt_negative(self):
		self.assertEqual(lib.sqrt(-1), 0)
        
unittest.main(verbosity=2)		
