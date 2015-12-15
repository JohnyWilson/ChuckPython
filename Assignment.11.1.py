# Welcome ... from Using Python to Access Web Data

# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and
# the other is the actual data you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 116 values with a sum=597873)
# Actual data: http://python-data.dr-chuck.net/regex_sum_172345.txt (There are 80 values and the sum ends with 301)

# These links open in a new window. Make sure to save the file into the same folder
# as you will be writing your Python program.
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
# Data Format

# The file contains much of the text from the introduction of the textbook except that random numbers
# are inserted throughout the text. Here is a sample of the output you might see:

# Why should you learn to write programs? 7746
# 12 1929 8827

# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...
# The sum for the sample text above is 27486. The numbers can appear anywhere in the line.
# There can be any number of numbers in each line (including none).
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to
# integers and summing up the integers.


import re

file = 'regex_sum_172345.txt'

summ = 0
item = 0
lines = open(file).readlines()

for line in lines:
    # number = re.findall(r'\b\d+\b', line);
    number = re.findall('[0-9]+', line)
    item += len(number)
    if len(number) != 0:
        for i in number:
            summ += int(i)
print 'There are ' + str(item) + ' values with a sum=' + str(summ)

summ2 = 0
count2 = 0
for item2 in re.findall('[0-9]+', open(file).read()):
    count2 += 1
    summ2 += int(item2)
print 'There are ' + str(count2) + ' values with a sum=' + str(summ2)

# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )