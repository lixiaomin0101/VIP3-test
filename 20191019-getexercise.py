# import requests
#
# urlstr ='https://blog.csdn.net/rainshine1190'
#
# r = requests.get(url=urlstr)
#
# print(r.text)


# import  requests
# urlstr ='http://www.wanandroid.com/article/query'
#
# payload ={'k':'Android'}
#
# r= requests.get(url=urlstr,params=payload)
#
# print(r.text)
# print(r.status_code)
#
# import requests,json
#
# urlstr = 'http://httpbin.org/post'
# payload = {'qq群名':'selenium+jmeter+oadrunner','qq群号':'106014970'}
# payload =json.dumps(payload)
# r = requests.post(url=urlstr,data=payload)
# #获取结果
# print(r.text)
# print(r.json())

import  requests,json

urlstr='http://httpbin.org/post'
payload={'qq群名':'selenium+jmeter+oadrunner','qq群号':'16014970'}
r = requests.post(url=urlstr,json= payload)
print(r.text)
print(r.json())