import urllib, urllib.request, sys
import urllib.parse
import ssl
# encoding:utf-8
import base64
# from token import access_token

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=w0wkTs9R7nyMUsOiSYaNxh99&client_secret=sGDhL9cKVlaIByxIz7wMDOYaO3H5C4Oh'
# request = urllib.request.Request(host)
# request.add_header('Content-Type', 'application/json; charset=UTF-8')
# response = urllib.request.urlopen(request)
# content = response.read()
# if (content):
#     print(content)


'''
人脸检测接口
'''

detectUrl = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
# 参数image：图像base64编码，max_face_num：最多处理人脸数目，默认值1，face_fields：包括age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities信息，逗号分隔，默认只返回人脸框、概率和旋转角度\
f=open(r'F:/image.png','rb') #二进制方式打开图文件
img=base64.b64encode(f.read())
params = {"max_face_num": 1, "face_fields": "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
          "image": img}

params = urllib.parse.urlencode(params).encode(encoding='UTF-8')
access_token = '24.a663959ff5b8a2754485df0eebacf849.2592000.1506420761.282335-9954285'
detectUrl = detectUrl + "?access_token=" + access_token
request = urllib.request.Request(url=detectUrl, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print(content)