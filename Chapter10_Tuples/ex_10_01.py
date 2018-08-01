# 1. File read
# 2. Compute words frequency
# 3. Descending sort order by values
# 4. Print the words top 5 frequency

# 1. File read
print('1. File read')
fh = open('clown.txt')
#fh = open('intro.txt')

# 2. Compute words frequency
print('\n2. Compute words frequency')
di = {}
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1
print(di)

# 3. Descending sort order by values
print('\n3. Descending sort order by values')
lst = []
for key, val in di.items():
    lst.append((val, key))
lst = sorted(lst, reverse=True)
print(lst)

# 4. Print the words top 5 frequency
print('\n4. Print the words top 5 frequency')
for freq in lst[:5]:
    print(freq)

print('\n%d' % lst[0][0])  # 7
print(lst[0][1])          # the