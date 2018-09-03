
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.flipkart.com")
bs = BeautifulSoup(resp.text)

for script in bs.find_all("script"):
        try:
           print(script['src'])
        except:
            pass






