import  requests

urlstr ='https://www.wanandroid.com/user/login'

payload={'username':'chaoge','password':'123456'}
r =requests.post(url=urlstr,data=payload)
print(r.text)
print()
print(type(r.json()))
print(r.json()['data']['username'])
if r.json()['data']['username']== payload['username']:
    print('登录成功')
