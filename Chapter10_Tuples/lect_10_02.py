fh = open('romeo.txt')

print('최다 출현 단어 계산')
counts = {}
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

print('Descending sort order by values using list')
lst = []
for key, val in counts.items():
    lst.append((val, key))

lst = sorted(lst, reverse=True)
print(lst)

print('List up 10 words of high frequency')
for high in lst[:10]:
    print(high)