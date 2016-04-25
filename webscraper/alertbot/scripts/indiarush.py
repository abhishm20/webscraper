from bs4 import BeautifulSoup
import requests

def get(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        block1 = soup.find_all('span',{'class':'product-price-view font-extra-large'}) #### return price 
        block2 = soup.find_all('h1',{'class':'font-normal  full-product-name'})#### return name 
        return [str(block2[0].text),str(str(block1[0].text)[3:])]
    except:
        message ="failed"
        return message
#print Price_Return(raw_input("enter the url \n "))


    
