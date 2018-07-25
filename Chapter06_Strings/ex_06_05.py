str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')  # find an index of the char ':'
piece = str[ipos+2:]  # store the value after the index in str
value = float(piece)  # type casting
print(value)