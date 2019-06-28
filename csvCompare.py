"""

Author: Prathmesh Phalke
Version: 2.4
Created on: 04/22/2019
Last Updated: 05/25/2019
"""

#imports
import csv
from collections import Counter

def csv_compare(firstFileString, secondFileString, hasHeader, delim, useableColumns): 
	"""
	takes in two csvs and information, compares them and returns a list of counted strings where items in the dict with count 2 are properly matched

	@param fileA is a string representing a file path
	@param fileB is a string representing a file path
	@param hasHeader is a boolean discribing if the files have headers
	@param delim is a string with the character that is the delimiter in the CSVs
	@param columns is and array with the numbers 1 and 0 representing which columns to use in the comparrison
	@return a dict of strings and there count representing matched rows
	"""

	firstFile = [] #array in which to write the old file
	secondFile = [] #array in which to write the new file

	#reading in first file
	with open(firstFileString, encoding = 'utf_8') as csv_file:

		csv_reader = csv.reader(csv_file, delimiter = delim)
		for row in csv_reader:
			firstFile.append(row)
		#removing the top row if there is a header.
		if hasHeader == 'yes':
			firstFile.pop(0)

	#reading in second file
	with open(secondFileString, encoding = 'utf_8') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter = delim)
		for row in csv_reader:
			secondFile.append(row)
		#removing the top row if there is a header. It's already saved off the old file
		if hasHeader == 'yes':
			secondFile.pop(0)

	#combines the two lists into one CSV 
	finalList = firstFile + secondFile

	#remove unwanted columns from the final list
	for x in range(len(finalList)):
		counter = 0
		for b in range(len(useableColumns)):
			if useableColumns[b] == 0:
				del finalList[x][b-counter]
				counter += 1
	
	for x in range(len(finalList)):
		finalList[x] = str(finalList[x])

	#counts occurences of items and returns it
	return Counter(finalList)

def compare_just_files(firstFileString, secondFileString):
	"""
	function operates as a runner of the csv comparer taking in the two file paths to be compared

	@param fileA is a string representing a file path
	@param fileB is a string representing a file path
	@return a dict of strings and there count representing matched rows
	"""	
	
	hasHeader = '' #yes if the csv's have a header, otherwise no
	header = [] #holds the header row if one exsists. is otherwise unused
	delim = '' #holds the delimiter for the files

	#takes header information in
	while hasHeader != 'yes' and hasHeader != 'no':
		print('do the csv\'s have headers? (yes/no)')
		hasHeader = input()
		#ensuring input is appropriate
		if hasHeader != 'yes' and hasHeader != 'no':
			print('please enter a valid response')

	#Takes delimiter information in
	print('what is the delimiter in the files?')
	delim = input()

	#Grabbing the header from the first file
	with open(firstFileString) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter = delim)
		header = next(csv_reader)

	useableColumns = determine_columns(hasHeader, header)

	return csv_compare(firstFileString, secondFileString, hasHeader, delim, useableColumns)

def determine_columns(hasHeader, header):
	"""
	function takes in header information and returns array representing which columns to ignore

	@param hasHeader is a boolean representing if the csvs hold a header row
	@param header is an array holding the top row of the files
	@return returns an array of 1's and 0's representing which columns should be used
	"""

	#Sets the Array to the correct length
	useableColumns = ['blank']*len(header)

	#Fills the useable column array with the columns that should be ignored
	for x in range(len(useableColumns)):
		while useableColumns[x] != 0 and useableColumns[x] != 1:
			#If there is a header that we can work with
			if hasHeader =='yes':
				print('should we compare column ' + header[x] +'? (0 for remove, 1 for keep)')
				temp = input()
				#ensuring input is appropriate
				if temp != '0' and temp != '1':
					print('please enter a valid response')
				else:
					useableColumns[x] = int(temp)
			#If there is no header we show data from the first row for decisions to be made
			elif hasHeader == 'no':
				print('should we compare column with data like ' + header[x] +'? (0/1)')
				temp = input()
				#ensuring input is appropriate
				if temp != '0' and temp != '1':
					print('please enter a valid response')
				else:
					useableColumns[x] = int(temp)

	return useableColumns

def intake(file):
	"""
	function to intake a file and format its inputs for a comparer.

	The file should be a csv (tilda delimited though you can change in the code below)
	It should have a header row with column titles 
	format should be file1 (file name to be compared), file2 (other file to be compared), hasHeader (yes or no),
	delimiter, usecolumn list (in form 111010011010 where 1's represent to use the column, 0's represent no to use the column)
	@param filename is a filepath
	@return an array that contains the components for running the comparison with minimal manual input
	"""

	returnArray = []

	#reading in the entire file
	with open(file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter = "~")#change here to switch delimiters
		for row in csv_reader:
			returnArray.append(row)
	
	#removing the top row (the Header)
	returnArray.pop(0)

	#editing the last entry in each list of the array to be a list
	for x in range(len(returnArray)):
		returnArray[x][4] = list(returnArray[x][4])

	#editing the last entry in each list of the array to be a list of ints rather than strings
	for x in range(len(returnArray)):
		for b in range(len(returnArray[x][4])):	
			returnArray[x][4][b] = int(returnArray[x][4][b])

	return returnArray

def compare_runner(runList):
	"""
	function operates as a runner of the csv comparer taking in a list with all the needed information to run the comparer in am array

	@param runList is an array that contains the components for running the comparison with minimal manual input
	"""

	for x in range(len(runList)):
		count = csvCompare.csv_compare(runList[x][0], runList[x][1], runList[x][2], runList[x][3], runList[x][4])

	#prints the counter if it does not equal 2
	for key, value in count.items():
		print(key, value)

	matchCounter = 0 # for calculating what percaentage of rows matched

	#calculates the number of matchs in the two csvs
	for key, value in count.items():
		if value == 2:
			matchCounter += 1

	#Final Statistics
	print('the total number of matched rows is ' +str(matchCounter))
	print('the percent of matched rows is ' + str(100 * float(matchCounter)/float(len(count))) + '%')

def basic_compare_runner(file1, file2):
	"""
	function operates as a runner of the csv comparer taking in two file paths to compare

	@param file1 is a string representing a file path for comparisson
	@param file2 is a string representing a file path for comparisson
	"""

	count = compare_just_files(file1, file2)

	#prints the counter if it does not equal 20
	for key, value in count.items():
		if value != 2:
			print(key, value)

	matchCounter = 0 # for calculating what percaentage of rows matched

	#calculates the number of matchs in the two csvs
	for key, value in count.items():
		if value == 2:
			matchCounter += 1

	#Final Statistics
	print('the total number of matched rows is ' +str(matchCounter))
	print('the percent of rows matched is ' + str(100 * float(matchCounter)/float(len(count))) + '%')

basic_compare_runner('C:\\Users\\pphalke\\OneDrive - Corporate Technologies Inc\\Documents\\HBP\\New\\AVALARA_EBS_2019-05.csv', 
	'C:\\Users\\pphalke\\OneDrive - Corporate Technologies Inc\\Documents\\HBP\\Old\\AVALARA_EBS_2019-05.csv')
