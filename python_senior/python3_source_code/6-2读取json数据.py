# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 11:21'
# import requests
# import json
#
# # 录音
# from record import Record
# record = Record
# audioData = record.record(2)
#
# # 获取token
# from secret import API_KEY, SECRET_KEY, token
# authUrl = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_" \
#           "id=” + API_KEY + “&client_secret=” + SECRET_KEY"
# response = requests.get(authUrl)
# res = json.load(response.content)
# token = res['access_token']
#
# # 语音识别
# cuid = "xxxxxxxxxx"
# srvUrl = "http://vop.baidu.com/server_api" + "?cuid=" + cuid + "&token=" + token
# httpHeader = {'Content-Type’:’audio/wav; rate = 8000'}
# response = requests.post(srvUrl,headers=httpHeader,data=audioData)
# res = json.loads(response.content)
# text = res['result'][0]
# print(u'\n识别结果:')

####################################################################################
import json
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data, sort_keys=True)  # 将python对象转换成json对象(string)
print(json_str)
data = json.loads(json_str)  # 将json对象转换成python对象
print(data)

# Writing JSON data file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)