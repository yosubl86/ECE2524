#!/usr/bin/python2
#ECE 2524 Homework 3 Problem 1 <Yosub Lee>
import sys
import argparse

parser = argparse.ArgumentParser(description='Process some numbers')
parser.parse_args()

#function to check whether it can be float type
def Tofloat(target):
	try:
		target = float(target)
		return target
	except ValueError as e:
		print e
		sys.exit(1)

#Main from here
num1 = raw_input("")
num1 = Tofloat(num1)
						
while True:
	try:
		num2 = raw_input("")
		if num2 != '':
				num2 = Tofloat(num2)
				mult = num1*num2
				num1 = mult	
		else:	
			print mult
			num1 = raw_input("")
			num1 = Tofloat(num1)

	except EOFError:
		print	mult
		sys.exit(0)

