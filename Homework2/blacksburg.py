#ECE 2524 Homework 2 Problem 2 <Yosub Lee>
import string

from sys import argv

script, filename = argv

company = open(filename)

location = 'Blacksburg'
comma = ', '

print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
for line in company.readlines():
    data = line.split()
    if data[3] == location:
        seq = (data[4], data[1], data[0], data[2])
        print comma.join(seq)
