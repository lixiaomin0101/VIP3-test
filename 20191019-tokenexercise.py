#第一种方式
# import requests
#
# urlstr='https://www.wanandroid.com/user/login'
#
# data ={'username':'liangchao','password':'123456'}
#
# # 发送请求
#
# r = requests.post(url=urlstr,data=data)
# print('*******',r.text)
# print('*******',r.cookies)
# print('*******',r.headers)
#
# #获取上次请求放回的response中的cookies，传递给下一次请求
#
# cookies=r.cookies
#
# r2 =requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies=cookie)
# print('*****',r2.text,r2.status_code)



#第二种方式
# import  requests
# urlstr='https://www.wanandroid.com/user/login'
#
# data ={'username':'liangchao','password':'123456'}
# #初始化session对象
#
# s=requests.session()
# #通过session发送请求，服务器设置在本地的Cookes保存在本地
#
# r=s.post(url=urlstr,data=data)
# r2 =s.get('https://www.wanandroid.com/lg/todo/list/0')
# print('*********',r2.text)
# print('*********',r.text)




#第三种方式
# import requests
# urlstr='https://www.wanandroid.com/user/login'
# data ={'username':'liangchao','password':'123456'}
#
# #发送请求
# r =requests.post(url=urlstr,data=data)
#
# print('*********', r.text)
#
# print(r.cookies['JESSIONID'])
# cookie ={
#     'JESSIONID':r.cookies['JESSIONID']
# }
# r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies=cookie)
#
# print('******', r2.text)
# print('******', r2.headers)




#第四种

import requests,re
urlstr='https://www.wanandroid.com/user/login'
data ={'username':'liangchao','password':'123456'}

#发送请求
r =requests.post(url=urlstr,data=data)

print('*********', r.text)
print('*********', r.cookies)
print('*********', r.headers)
print(r.cookies['JESSIONID'])
header = {
    'cookie':'JESSIONID='+r.cookies['JESSIONID']
}
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',headers=header)
print('******', r2.text)
print('******', r2.headers)

result =r2.text.find("已完成清单")
print(result)
if result != -1:
    print('查询成功')
else:
    print('查询失败')