import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://www.dr-chuck.com'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # A text starting with 'href' or None(default)
    print(tag.get('href', None))
'''
https://www.dr-chuck.com/csev-blog/
https://www.si.umich.edu/
https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1159280
https://www.dr-chuck.com/csev-blog/
https://www.twitter.com/drchuck/
https://www.dr-chuck.com/dr-chuck/resume/speaking.htm
https://www.slideshare.net/csev
/dr-chuck/resume/index.htm
https://amzn.to/1K5Q81K
http://afs.dr-chuck.com/papers/
https://itunes.apple.com/us/podcast/computing-conversations/id731495760
https://www.youtube.com/playlist?list=PLHJB2bhmgB7dFuY7HmrXLj5BmHGKTD-3R
https://developers.imsglobal.org/
https://www.youtube.com/user/csev
https://vimeo.com/drchuck/videos
https://backpack.openbadges.org/share/4f76699ddb399d162a00b89a452074b3/
https://www.linkedin.com/in/charlesseverance/
https://www.researchgate.net/profile/Charles_Severance/
https://www.tsugicloud.org/
/office
https://www.coursera.org/course/pythonlearn
https://www.coursera.org/course/insidetheinternet
https://open.umich.edu/education/si/si502/winter2009/
http://www.pythonlearn.com
http://www.php-intro.com/
http://www.appenginelearn.com/
http://www.pythonlearn.com/
/sakai-book
http://www.amazon.com/gp/product/1624311393/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1624311393&linkCode=as2&tag=drchu02-20
http://www.amazon.com/gp/product/059680069X/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=059680069X&linkCode=as2&tag=drchu02-20
http://www.amazon.com/Performance-Computing-Architectures-Optimization-Benchmarks/dp/156592312X/
http://oreilly.com/catalog/9781565923126/
http://cnx.org/content/col11136/latest/
http://www.youtube.com/playlist?list=PLHJB2bhmgB7dFuY7HmrXLj5BmHGKTD-3R
https://www.vimeo.com/17207620
https://www.youtube.com/watch?v=BVKpW02hsrU
https://www.youtube.com/watch?v=sa2WsgCvn7c
https://www.vimeo.com/17213019
https://www.youtube.com/watch?v=FJ078sO35M0
http://afs.dr-chuck.com/citoolkit
https://www.sakaiproject.org/
https://www.tsugi.org/
https://developers.imsglobal.org/
/obi-sample
https://twitter.com/drchuck
'''