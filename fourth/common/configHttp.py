# coding:utf-8
import  requests
class configHttp():
    def get(self,url,param):
        try:
            repone = requests.get(url,params=param)
            result =repone.text
            return result
        except Exception:
            print("请求报错")
            return None
    def post(self,url,param):
        try:
            repone = requests.post(url, param)
            result = repone.text
            return result
        except Exception:
            print("Post请求报错")
            return  None
    def request(self,url,param,method):
        if method =='get':
            return self.get(url,param)
        if method =='post':
            return self.post(url,param)

ceshi =configHttp()
# url='https://www.baidu.com/'
# url='https://www.wanandroid.com/user/logout/json'
# param={'username':'liangchao'}
# print(param)
# r = ceshi.request(url,param,'get')
# print(r)
#
# url='https://www.wanandroid.com/user/login'
# param={'username':'liangchao','password':'123456'}
# print(param)
# r = ceshi.request(url,param,'post')
# print(r)