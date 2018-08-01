# List: lst = list() / lst = []
# Dictionary: dic = dict() / dict = {}
# Tuple: tpl = tuple() / tpl = ()

## Sorting by keys
d = {'b':1, 'a':10, 'c':22}
print('Dictionary')
print(d.items())
# dict_items([('b', 1), ('a', 10), ('c', 22)])
print('Sorting by keys')
print(sorted(d.items()))
# [('a', 10), ('b', 1), ('c', 22)]

## Sorting by values
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for v, k in c.items():
    tmp.append((v, k))

print('List')
print(tmp)

print('Sorting by values')
tmp = sorted(tmp)
print(tmp)

print('Sorting by values, reverse')
tmp = sorted(tmp, reverse = True)
print(tmp)