counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name in counts:  # Compare 'name' and 'counts'
        counts[name] = counts[name] + 1
    else :
        counts[name] = 1

print(counts)
