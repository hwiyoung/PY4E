name = input('Enter file: ')
fh = open(name)

counts = dict()
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

# Initialization
bigword = None
bigcount = None
# Counting
for word, count in counts.items():
    # counts dict에서 value(count)의 최고값을 판단
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)