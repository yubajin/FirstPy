html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import urllib.request
import re
from bs4 import BeautifulSoup

url = 'http://139.199.212.114'
response = urllib.request.urlopen(url)
content = response.read()
print(content)
soup = BeautifulSoup(html_doc,'html.parser')

# print(soup.prettify())
print("soup.title:",soup.title)
print("soup.title.parent.name:",soup.title.parent.name)
print('<',soup.title.name,'>:',soup.title.string)

print('获取所有链接')
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())

print('获取only lacie')
link_node = soup.find('a',href='http://example.com/lacie')
print(link_node.name,link_node['href'],link_node.get_text())

print('正则表达式获取')
link_node = soup.find('a',href=re.compile(r'ill'))
print(link_node.name,link_node['href'],link_node.get_text())

print('get_p')
p_node = soup.find('p',class_='title')
print(p_node.name,p_node.get_text())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link2">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>