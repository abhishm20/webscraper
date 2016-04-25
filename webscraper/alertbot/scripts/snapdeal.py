from bs4 import BeautifulSoup
import requests

def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        block1 = soup.find_all('span',{'class':'payBlkBig'})
        block2 = soup.find_all('h1',{'itemprop':'name'})
        return [str(block2[0].text),block1[0].text.replace(",","")]
    except:
        message = "failed"
        return message
