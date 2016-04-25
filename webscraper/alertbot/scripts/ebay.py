from bs4 import BeautifulSoup
import requests

def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        block1 = soup.find_all('span',{'id':'prcIsum'})
        block2 = soup.find_all('h1',{'class':'it-ttl'})
        return [str(block2[0].text[16:]),block1[0].text[4:].replace(",","")]
    except:
        message = "failed"
        return message
