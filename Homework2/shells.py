# ECE 2524 Homework 2 Problem 1 <Yosub Lee>
import string

passwd = open('/etc/passwd')
for line in passwd.readlines():
    rec = string.splitfields(line, ':')
    print "%s %s" % (str(rec[0]).ljust(20), str(rec[6]).rstrip('\n'))
    
   
