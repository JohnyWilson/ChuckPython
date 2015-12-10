
# Question 1
#Hours = int(raw_input('Enter Hours: '))
#Rate = float(raw_input('Enter Rate: '))
#if Hours > 40:
#    Rate *=1.5
#print 'Gross Pay: ' + str(Hours*Rate)

# Question 2
try:
    Hours = int(raw_input('Enter Hours: '))
except:
    print('Error, please enter numeric input')
    exit()

try:
    Rate = float(raw_input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    exit()

if Hours > 40:
    Rate *=1.5
print 'Gross Pay: ' + str(Hours*Rate)

# Question 3


# Question 4
width = 17
height = 12.0
print width/2, type(width/2)
print width/2.0, type(width/2.0)
print height/3, type(height/3)
print 1+2*5, type(1+2*5)

# Question 5: Code for C to F conversion
#print 'Temperature in Celcuis is: ' + str((5.0/9.0)*(float(raw_input('Enter Celcius Temerature: '))-32))