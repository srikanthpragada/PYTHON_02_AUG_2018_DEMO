
import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text,"xml")

for item in bs.find_all("item"):
     print(item.find("title").text)
     print(item.find("pubDate").text)
     print(item.find("link").text, end="\n\n")




