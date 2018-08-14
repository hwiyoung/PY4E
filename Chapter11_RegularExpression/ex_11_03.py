### Extract the host of the email
'''
# Using 'find' method
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # 21
sppos = data.find(' ',atpos)
print(sppos) # 31
host = data[atpos+1 : sppos]
print(host) # uct.ac.za

# Using 'split' method
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split() # split by space
email = words[1]
pieces = email.split('@')
print(pieces[1]) # 'uct.ac.za'
'''

# Using regular expression
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# From으로 시작하는 문자열 중에서
# @으로 시작하고
# 공백을 포함하기 전까지의 문자열
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

# ['uct.ac.za']