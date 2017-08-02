#!/usr/bin/env python

########################################################################
# Find 'pi' to 'nth' precision
#
# @author: Satish Dash
#
########################################################################

import decimal 

class PiToNthPrecision(object):
	def __init__(self, n):
		self.n = n
		self.numerator = 22
		self.denominator = 7

	def _compute(self):
		decimal.getcontext().prec += 2
		three = decimal.Decimal(3) # 3 decimal places for default
		last, t, s ,n, na, d, da = 0, three, 3, 1, 0, 0, 24
		while  last != s:
			last = s
			n, na = n+na, na+8
			d, da = d + da, da + 32
			t = (t * n)/d
			s += t
		decimal.getcontext().prec -= 2
		return +s
	
	def find(self):
		decimal.getcontext().prec = self.n + 1
		return self._compute()

if __name__ == "__main__":
	n = int(input("Enter the nth place for calculating the precision: ").strip())
	piObj = PiToNthPrecision(n)
	print("The value of PI to {} precision is: {}".format(n, piObj.find()))
