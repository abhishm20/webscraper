from bs4 import BeautifulSoup
import requests
import time

def get(url):
    try:
        print url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        block1 = soup.find_all('span',{'id':'hs18Price'})
        print block1
        for i in block1:
            print i
    except Exception as e:
        message = "failed"
        return message


##def Refresh(time,ExPrice):
##    While True:
##        price = Method(raw_input("enter the url \n"))
##        if price <= ExPrice:
##            sendMsg()
##            break
##        else:
##            time.sleep(time)
##Refresh (int(raw_input("Enter Refresh Time In sec")),int(raw_input("Expected Price")))
