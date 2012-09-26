#!/usr/bin/python2
#ECE 2524 Homework 3 Problem 2 <Yosub Lee>
#This code looks so ugly. but this is the best way that I can do right now. sorry.

import sys
import argparse
import string
import fileinput

#function to check whether it can be float type
def Tofloat1(target):	
		try:
			target = float(target)
			return target
		except ValueError as e:
			print e
			sys.exit(1)
	
#Function for flag 'ignore blank'
def Tofloat2(target):
	if target != '\n':		
		try:	
			target = float(target)
			return target
		except ValueError as e:
			print e
			sys.exit(1)
	else:
		return 1

#Function for flag 'ignore bad number'
def Tofloat3(target):
	if target != '\n':
		try:
			target = float(target)
			return target
		except ValueError:
			return 1	
	else: 
		print mult
		return 1
#function for 'ignore every bad-things!'
def Tofloat4(target):
	try:
		target = float(target)
		return target
	except ValueError:
		target = 1
		return target
		
#multiply. but gets number from command line [same as problem1]
def stdin_mult():
	num1 = raw_input("")
	num1 = Tofloat1(num1)						
	while True:
		try:
			num2 = raw_input("")
			if num2 != '':
					num2 = Tofloat1(num2)
					mult = num1*num2
					num1 = mult	
			else:	
				print mult
				num1 = raw_input("")
				num1 = Tofloat1(num1)

		except EOFError:
			print	mult
			sys.exit(0)


parser = argparse.ArgumentParser(description='Process some numbers')
parser.add_argument('--ignore-blank', action='store_const', const = 'blank')
parser.add_argument('--ignore-non-numeric', action='store_const', const = 'numeric')
parser.add_argument('file1', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('file2', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()


#Main Starts here
mult1 = 1			#for the first input file
mult1 = float(mult1)

mult2 = 1			#for the second input file
mult2 = float(mult2)

mult = 1			#for the first * the second
mult = float(mult)

#for the first input file
if (args.file1 != sys.stdin):
	if args.ignore_non_numeric == 'numeric' and args.ignore_blank == 'blank':
		for line in args.file1.readlines():
			num1 = Tofloat4(line)
			mult1 = mult1 * num1
			mult = mult1 * mult2			
	if args.ignore_blank == 'blank':	
		for line in args.file1.readlines():
			num1 = Tofloat2(line)
			mult1 = mult1 * num1
			mult = mult1 * mult2
	if args.ignore_non_numeric == 'numeric':
		for line in args.file1.readlines():
			num1 = Tofloat3(line)
			mult1 = mult1 * num1
			mult = mult1 * mult2
	else:
		for line in args.file1.readlines():
			if line == '\n':
				print mult1
				mult1 = 1
				num1 = 1
			else:								
				num1 = Tofloat1(line)
				mult1 = mult1 * num1
else:
	stdin_mult() 


#for the second file input
if args.file2 != sys.stdin:
	if args.ignore_non_numeric == 'numeric' and args.ignore_blank == 'blank':
		for line in args.file2.readlines():
			num2 = Tofloat4(line)
			mult2 = mult2 * num2
	if args.ignore_blank == 'blank':	
		for line in args.file2.readlines():
			num2 = Tofloat2(line)
			mult2 = mult2 * num2
	if args.ignore_non_numeric == 'numeric':
		for line in args.file2.readlines():
			num2 = Tofloat3(line)
			mult2 = mult2 * num2
	else:
		for line in args.file2.readlines():
			if line == '\n':						
				print mult2
				mult2 = 1
				num2 = 1
			else:				
				num2 = Tofloat1(line)
				mult2 = mult2 * num2
else:
	mult2 = 1

#calculate total multi.
mult = mult1 * mult2

print mult


