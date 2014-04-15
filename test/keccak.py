
import unittest
from .. import keccak 

SHA3 = keccak.Keccak

class TestSHA3(unittest.TestCase):

	def empty():
		self.assertTrue(SHA3(256)("").hexdigest() == "0xa7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a")

	def basic():
		self.assertTrue(SHA3(256)("The quick brown fox jumps over the lazy dog").hexdigest() == "0x69070dda01975c8c120c3aada1b282394e7f032fa9cf32f4cb2259a0897dfc04")
		self.assertTrue(SHA3(256)("The quick brown fox jumps over the lazy dog.").hexdigest() == "0xa80f839cd4f83f6c3dafc87feae470045e4eb0d366397d5c6ce34ba1739f734d")
