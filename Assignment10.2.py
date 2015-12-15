# Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1: name = "Data/mbox-short.txt"
handle = open(name).readlines()
# handle = open("Data/mbox-short.txt").readlines()

TimeList = list()
Timecount = {}

for line in handle:
    if line.startswith("From "):
        splitline = line.rstrip("\n").split(" ")[6].split(":")
        TimeList.append((splitline[0], splitline[2]))

for k,v in TimeList:
    Timecount[k] = Timecount.get(k,0)+1

Dicti = Timecount.items()
Dicti.sort()

for a,b in Dicti:
    print a, b