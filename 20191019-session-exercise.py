import  requests
urlstr='https://www.wanandroid.com/user/login'
data={'username':'liangchao','password':'123456'}
s= requests.session()
r=s.post(url=urlstr,data=data)
r2 =s.get('https://www.wanandroid.com/lg/tobao/list/0')

print('*****'r2.text)
print('******',r.text)