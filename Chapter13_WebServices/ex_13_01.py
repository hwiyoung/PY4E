import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
#User count: 2

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)   # tag - text
    print('Attribute:', item.get('x'))  # attribute
'''
Name: Chuck
Id: 001
Attribute: 2
Name: Brent
Id: 009
Attribute: 7
'''