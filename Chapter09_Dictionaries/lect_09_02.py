counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
    # counts.get(name, 0)의 의미
    # counts 딕셔너리에 name이라는 키가 존재할 경우 name에 대한 값(value)을 불러오고,
    # 그렇지 않을 경우에는 counts 딕셔너리에 name이라는 키에 0을 추가

print(counts)