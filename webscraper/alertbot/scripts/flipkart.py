from bs4 import BeautifulSoup
import requests

def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        block1 = soup.find_all('span',{'class':'selling-price omniture-field'})
        block2 = soup.find_all('h1',{'class':'title'})
        return [str(block2[0].text),block1[0].text[4:]]
    except:
        message = "failed"
        return message

#print(get(raw_input('enter url: ')))
