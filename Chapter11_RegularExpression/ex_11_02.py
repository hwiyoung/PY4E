# Finding patterns in specific condition
import re

###
x = 'My 2 favorite numbers are 19 and 42'
# 0에서 9에 해당하는 문자 검색
y = re.findall('[0-9]+',x)
print(y)

# AEIOU에 해당하는 문자 검색(대소문자 구별)
y = re.findall('[AEIOU]+',x)
print(y)

###
x = 'From: Using the : character'
# F로 시작하고 :로 끝나는 패턴 찾기(Greedy)
y = re.findall('^F.+:', x)
print(y)

# F로 시작하고 :로 끝나는 패턴 찾기(Non-greedy)
y = re.findall('^F.+?:', x)
print(y)

###
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# @ 전후로 공백전까지 찾기
y = re.findall('\S+@\S+',x)
print(y)

# 소괄호를 통해 찾는 범위 제한
y = re.findall('^From (\S+@\S+)',x)
print(y)