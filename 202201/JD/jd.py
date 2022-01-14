import requests

import time
import random


def nian(ck, data):
	data += '&client=wh5&clientVersion=1.0.0'
	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Origin': 'https://wbbny.m.jd.com',
		'User-Agent':r'jdapp;android;10.3.2;;;appBuild/92141;ef/1;ep/{"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","ts":1642086837451,"ridx":-1,"cipher":{"sv":"CJO=","ad":"ZJCyYWU5DNO5CQDuZtU2YG==","od":"YtLsYtO3DQYyZJZuEJK4EK==","ov":"CzK=","ud":"ZJCyYWU5DNO5CQDuZtU2YG=="},"ciphertype":5,"version":"1.2.0","appname":"com.jingdong.app.mall"};jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 11; 21091116C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045735 Mobile Safari/537.36',
		'Cookie': ck,
		'Host': 'api.m.jd.com',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Referer': 'https://wbbny.m.jd.com/babelDiy/Zeus/41AJZXRUJeTqdBK9bPoPgUJiodcU/index.html?babelChannel=syfc&from=home',
	    'Content-Length': str(len(data)),
	    'X-Requested-With': 'com.jingdong.app.mall',
	    'Connection': 'keep-alive',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-site',
	}
	url = 'https://api.m.jd.com/client.action?functionId=tigernian_collectAutoScore'
	response = requests.post(url, headers=headers, data=data)
	print(response.text)


# 填cookie\data即可
ck = 'pt1'
data = r'body={"ss":"{\"extraData\":{\"log\":\"164332034\"}"}'

while True:
	nian(ck, data)
	print('完成一轮')
	time.sleep(60*30)
