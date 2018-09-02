# Making the web browser using python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# (http://)(www.dr-chuck.com)(/page1.htm)
# (protocol)      (host)       (document)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
    '''
    HTTP/1.1 200 OK
    Date: Wed, 29 Aug 2018 04:31:22 GMT
    Server: Apache/2.4.18 (Ubuntu)
    Last-Modified: Sat, 13 May 2017 11:22:22 GMT
    ETag: "a7-54f6609245537"
    Accept-Ranges: bytes
    Content-Length: 167
    Cache-Control: max-age=0, no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: Wed, 11 Jan 1984 05:00:00 GMT
    Connection: close
    Content-Type: text/plain
    
    But soft what light through yonder window breaks
    It is the east and Juliet is the sun
    Arise fair sun and kill the envious moon
    Who is already sick and pale with grief
    '''
    #print(data)
mysock.close()