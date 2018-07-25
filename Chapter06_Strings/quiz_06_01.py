words = 'Connect Foundation'

if 'F' in words:
    words.lower()
    #words[7] = '&'  # TypeError: 'str' object does not support item assignment
    words.replace(words[7],'&')
else:
    print(words)
print(words)  # str function does not affect the original string