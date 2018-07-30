fh = open('mbox-short.txt')
# File Handle
# 1. 텍스트 파일을 읽는 하나의 표준화된 형태
# 2. 순차적으로 텍스트 파일을 읽음

for lx in fh:
    ly = lx.rstrip()  # print function adds line alignment in each line... have to remove it
    print(ly)