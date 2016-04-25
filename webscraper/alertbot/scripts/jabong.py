from bs4 import BeautifulSoup
import requests

def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        block1 = soup.find_all('span',{'itemprop':'price'})## price
        block2 = soup.find_all('span',{'itemprop':'name'})   ##name
        return [str(block2[0].text),str(block1[0].text)]
    except Exception as e:
        message ="failed"
        return message
#print Price_Return(raw_input("enter the url \n "))


    
