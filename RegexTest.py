import re

file = 'regex_sum_42.txt'

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)

print y, '\n'
