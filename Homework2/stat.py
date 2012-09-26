#ECE 2524 Homework 2 Problem 3 <Yosub Lee>
import string

from sys import argv
script, filename = argv
company = open(filename)

theSum = 0   #sum will be stored here
next_num = 0    #this variable will be used for comparison
max_num = 0
min_num = 100
count = 0 #to figure out how many data I have.

print "ACCOUNT SUMMARY"
for line in company.readlines():
    data = line.split()
    count = count + 1
    next_num = float(data[2])
    theSum = theSum + float(data[2])
    if next_num > max_num:
        max_num = next_num
        max_name = data[1]
    if next_num < min_num:
        min_num = next_num
        min_name = data[1]

print "Total amount owed =",theSum
print "Average amount owed =", theSum/count
print "Maximum amount owed =", max_num, "by",max_name
print "Minimum amount owed =", min_num, "by",min_name

