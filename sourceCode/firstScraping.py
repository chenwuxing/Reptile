
from bs4 import BeautifulSoup
import requests
import os
import re
os.makedirs('./img/', exist_ok=True)

URL = "http://www.netbian.com/"
headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"}
html = requests.get(URL,headers = headers)

html.encoding = html.apparent_encoding


soup = BeautifulSoup(html.text, "lxml")

target = soup.find_all("a",{"target":"_blank"})
target = soup.find_all("img")

for imgUrl in target:
    oneUrl = imgUrl["src"]
    response = requests.get(oneUrl,headers = headers)
    imgName = oneUrl[-10:]
    path = './img/'
    save = path + imgName
    with open(save,"wb") as f:
        f.write(response.content)
      








   








    
