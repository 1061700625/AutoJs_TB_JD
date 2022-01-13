import requests


def nian(ck):
	data = r'body={"ss":"{\"extraData\":{\"log\":\"1642086876821~1hXuSKsnBDgMDFwTWFFYTAxMQ%3D%3D.QXtVd1FIe1l2WUB4VTtUJygHMSYUfRgcH0FhVmlYXHwfdx9BMxAdNzcoMxcnCSwDBEw9HRYJGF0iGzYgDg%3D%3D.1f214947~9%2C1~E8944FF84FDC93C4CFF4FE2F19F4960B47AA1A74~0zm3pjj~C~ThRFWhIObG8cF0wPWRYNbkRRBhgMbB12YRhkcAAZTU1AFhsXAgAaAW0aCG4cYQQKHAQWUQQEG0FEGRVRAhsFbxwNbh5lAWBNBRoHBVYZQxdoGhNQQloVCAEZGhJHFg0XVwMDBwUOBw8DAw4FAg0IUAYWGxcRUFMXDxRFQ0RAQ1RFUxpNFkNSVEQPFVNTQkVDREFWEBwXSAVaFg1uVwUbBgAGHQUcBxsDHABlTRZeXRdcBBsXVkUTDRIMBwYHBwBYDFcPB1QCVFcDUgAOBAwAAAYACVIEAgYDURcbF1tGEw0SeF5cRU0YAFVGVF1QARUZF0ITDQECAwAADQ5ZAwIPB1cZFV9eFAsVHRlSAQJUXVgABQ4FBVFRAANXHFFRBwcKBlAMBFACBwwCV1FXAg5QAwkHBQQEBggDUAMPDFYGAgwXGhNRQFYVCBJEYDdzUWVnIExWV3QbfGdHeE4fX09LIBYYFVsQFw0XclleUFxRF3teVhZDGBZZVBAXDRcMBAADARYbEENWSkMObw8CVRkEDAZrHRVCWxUIaxcKUAQNBgRXA3QXGRRQWVRGWFtUFxRDBQUVGUQEBxsGGAMVHBYOAAEBCUMYFgIDVQYFBgQABAEJBwMBAQYVWAcEBAZQAQEDAwMCAQMFARAcFwlDaRgVXAlUFQ8XUFdRVlJRRkQXFENVXhUPREAVGRdVWBUKFkABHgEWURYYFVYAakEXDxQBBhIYFVBUFwJDRlVZUQlYCgEMBAICBwUPEBwXVQsWDmwHSgUbBWgaE1VcW1AQChcJVwAGBw1QDQcFAQ4HSQF3B2sEUGhZV1lZV1BQAFEDBwEPUwYOAVQBXFMMA1NWVVAEAQJSUFFRVwZMSRkJH0pKdUs1XXF2cEFeZWUFBlZ4BAkAZmJEUDFZDlNjZHhRdVh2YXNNfgdlBVRRM2BTcG1aQXZ4WHl0YlkBOGVDQ2Q%2BBEBQYnAAc2ZyA1Zjc2oCd1h5US5ebXZiBwRvZWYCYWhZbiJsWEdgLgRlYmdaVVRoX3VlYV5iB2xiT3cjXUBnYE58fHUFfmF4Z3IwYlkGciNCWGd0d3hkeFx9dXVSVzN1dWJ8JE1yVnAHXXV1U1BhcWdPJXFcA2Y%2BBXZkdl57ZmUFfWZ1TQAyYVhcZyVddWF0XgV1eFN2YWRCBVxKBAVDVlxPRRcaE1pDUxUIEhdF~1jiy0fq\",\"sceneid\":\"ZNShPageh5\"},\"secretp\":\"gnxRyU4oAhBB7V_3JfKfFC8\",\"random\":\"49235718\"}"}&client=wh5&clientVersion=1.0.0'
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



# 填cookie即可
# ck可以用httpcany抓取。
# 如果替换ck后不能用，可以抓包再替换data、User-Agent、Referer这些试试。
ck = '123'
import time
while True:
	nian(ck)
	print('休息30分钟')
	time.sleep(60*30)
	


