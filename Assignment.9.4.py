#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"

name = "Data/mbox-short.txt"
handle = open(name)
sender = dict()
MaxUser = ' '
MaxCount = 0

for line in handle:
    if line.startswith("From "):
        FromAdr = line.rstrip('\n').split(' ')[1]
        sender[FromAdr] = sender.get(FromAdr,0) + 1
       # if FromAdr in sender.keys():             sender[FromAdr] += 1
       # else:               sender[FromAdr] = 1

for adr, count in sender.items():
    if count == max(sender.values()):
        MaxUser = adr
        MaxCount = count

print MaxUser, MaxCount