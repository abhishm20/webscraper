from bs4 import BeautifulSoup
import requests

def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        block1 = soup.find_all('span',{'class':'cinch_price_amount webprz'})
        block2 = soup.find_all('span',{'class':'prodtitlenew'})
        return [str(block2[0].text),block1[0].text]
    except:
        message = "failed"
        return message
