# Use the file name mbox-short.txtmbox-short.txt as the file name
#fname = raw_input("Enter file name: ")
fh = open("mbox-short.txt")
count = 0
FloatSum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count+=1
    FloatSum = FloatSum + float(line.rstrip().split()[1])
print "Average spam confidence: ", FloatSum/count
