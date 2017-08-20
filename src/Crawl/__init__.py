import urllib.request
import http.cookiejar
url = "http://www.baidu.com"
 
print("第一种方法")
response1 = urllib.request.urlopen(url)
print (response1.getcode())
print (len(response1.read()))
'''
print('第二种方法')
# 创建Request对象
request = urllib.request.Request(url)
#添加数据    
request.data = 'a'
#添加http的header #将爬虫伪装成Mozilla浏览器
request.add_header('user-agent','Mozilla/5.0')
#发送请求获取结果
response2 = urllib.request.urlopen(request)
print (response2.getcode())
print (len(response2.read()))
'''

print('第三种方法')
cj = http.cookiejar.CookieJar()
#创建一个opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#给urllib安装opener
urllib.request.install_opener(opener)
#使用带有cookie的urllib访问网页
response3 = urllib.request.urlopen(url)
print (response3.getcode())
print (cj)
print (response3.read())
