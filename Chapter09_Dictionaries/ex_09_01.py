# 딕셔너리를 활용한 데이터 빈도수 측정
fh = open('clown.txt')

di = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

print(di)

largest = -1
theword = None
for key, value in di.items():
    if value > largest:  # 단어의 개수가 최대값보다 크면
        largest = value
        theword = key

print(theword, largest)