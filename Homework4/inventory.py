#!/usr/bin/python2
#ECE 2524 Homework 4 <Yosub Lee>

import sys 
import argparse
import string
import ast
import shlex

#array for data
PartID = []
Description = []
Footprint = []
Quantity = []
temp_storage = []


parser = argparse.ArgumentParser(description = 'Analyzing and edtting a Table txt file')
parser.add_argument('-f', '--data-file', dest='file', help="Path to the data file to read at startup")
args = parser.parse_args()

def read_data():
	readfile = open(sys.argv[2], 'r')
	for line in readfile:
		line = line.rstrip()
		temp_storage.append(line)
		line = shlex.split(line)
		PartID.append(line[0])
		Description.append(line[1])
		Footprint.append(line[2])
		Quantity.append(line[3])

def write_data():
	writefile = open(sys.argv[2], 'w')
	for line in temp_storage:
		writefile.write(line + "\n")		

def set_data(command):
	line = command.lstrip('set').strip()
	if "for" in line:
		line = line.split("for")
	what = line[0].split("=")	#before 'for'
	where = line[1].split("=")	#after 'for'
	index_num = PartID.index(where[1].strip()) #index number			
	target2 = where[1].strip()	#PartID 
	print "what: ", what[0].strip()
	print "where: ", where
	if( what[0].strip() == 'Quantity'):
		Quantity[index_num] = what[1].strip()
		temp_storage[index_num] = PartID[index_num] + "\t" + Description[index_num] + "\t" + Footprint[index_num] + "\t" + Quantity[index_num]
	elif( what[0].strip() == "Description"):
		Description[index_num] = what[1].strip()
		temp_storage[index_num] = PartID[index_num] + "\t" + Description[index_num] + "\t" + Footprint[index_num] + "\t" + str(Quantity[index_num])
	elif( what[0].strip() == "Footprint"):
		Footprint[index_num] = what[1].strip()
		temp_storage[index_num] = PartID[index_num] + "\t" + Description[index_num] + "\t" + Footprint[index_num] + "\t" + str(Quantity[index_num])
	elif( what[0].strip() == "PartID"):
		PartID[index_num] = what[1].strip()
		temp_storage[index_num] = PartID[index_num] + "\t" + Description[index_num] + "\t" + Footprint[index_num] + "\t" + str(Quantity[index_num])				
	else:
		print "Error: Could not find object"			
			
def add_data(command):
	line = command.lstrip('add').strip()
	line = ast.literal_eval(line)
	PartID.append(line['PartID'])
	Description.append(line['Description'])
	Footprint.append(line['Footprint'])
	Quantity.append(line['Quantity']) 
	temp_storage.append(line['PartID']+"\t"+line['Description']+"\t"+line['Footprint']+"\t"+str(line['Quantity']))


def remove_data(command):
	line = command.lstrip("remove").strip()
	ID = line.split("=")
	index_num = PartID.index(ID[1])
	temp_storage.pop(index_num)
	PartID.pop(index_num)
	Description.pop(index_num)
	Footprint.pop(index_num)
	Quantity.pop(index_num)
	write_data()

def print_data(command):
	if "remove" in line:
		line = line.split("for")

#main
if(args.file):
	read_data()
	print "[Command]\nlist: Print out table data\nadd: Add new data\nRemove: delete data\nSet: change and update data\nq: Quit"	
	while(1):
		try:
			command = raw_input(">>")
			
			if command.startswith('list'): #need to change
		#		line = command.lstrip('list all').strip()
		#		if 'with' in line:
		#			line = line.split("=")					
		#			if 'Footprint' in line[0]:
		#			
		#		elif 'sort' in line:
		#			line = line.strip()
		#			print line[0]
		#		else:
		#			print line				
				for output in temp_storage:
					print output
					
			if command.startswith('remove'):
				remove_data(command)
	
			if command.startswith('add'):	
				add_data(command)

			if command.startswith('set'):
				set_data(command)

			if command == "q":
				print "Bye Bye!"
				sys.exit(0)
			
			print "OK!"

		except ValueError as e:
			print e
			sys.exit(1)
