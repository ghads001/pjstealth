import requests
import urllib.parse
import random

token = "54e88bca11504c90b8a184e06c3d89ac7814f7e9a4d"

link = "https://httpbin.co/anything"

targetUrl = urllib.parse.quote(link)

super = "true"

geoCode = "de"

#regionalGeoCode = "europe"
#asia 亚洲 europe 欧洲 africa 非洲  oceania 大洋洲 northamerica 北美 southamerica 南美洲  
sessionId = str(random.randint(2000, 4000))

timeout = "120000"   # 5000 毫秒和 120000 毫秒

device = "mobile"   # desktop 和 mobile 

customWait = "35000"

render = "true"

height = "1280"
width = "720"

blockResources = "false"
customHeaders = "true"

url = "http://api.scrape.do?token={}&url={}&super={}&geoCode={}&sessionId={}&timeout={}&device={}&customWait={}&render={}&blockResources={}&width={}&height={}&customHeaders={}".format(token, targetUrl, super, geoCode, sessionId, timeout, device, customWait, render, blockResources, width, height, customHeaders)
payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Linux; Android 9; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.3527.52 '
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
