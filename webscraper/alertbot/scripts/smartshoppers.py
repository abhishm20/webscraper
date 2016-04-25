from bs4 import BeautifulSoup
import requests

def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        block1 = soup.find_all('span',{'class':'price'})## price
        block2 = soup.find_all('div',{'class':'product-name'})   ##name
        return [str(block2[0].text).replace('\n','').replace('\t',''),str(block1[1].text.replace(',','').replace(' ','')[4:][:-3])]
    except Exception as e:
        message ="failed"
        return message
#print Price_Return(raw_input("enter the url \n "))


    
