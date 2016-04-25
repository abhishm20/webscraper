from bs4 import BeautifulSoup
import requests


def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        block1 = soup.find_all('span',{'id':'priceblock_saleprice' or 'priceblock_ourprice'})
        block2 = soup.find_all('span',{'id':'productTitle'})
        return [str(block2[0].text),block1[0].text.encode('ascii','ignore').replace("," or '?',"")]
    except:
        message = "failed"
        return message
