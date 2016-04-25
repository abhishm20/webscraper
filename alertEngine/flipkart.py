from bs4 import BeautifulSoup
import requests
import sys

print sys.argv
r = requests.get(sys.argv[0])
soup = BeautifulSoup(r.content,'html.parser')
block1 = soup.find_all('span',{'class':'selling-price omniture-field'})
block2 = soup.find_all('h1',{'class':'title'})
print([str(block2[0].text),block1[0].text[4:]])

# def get(url):
#     try:
#
#     except:
#         message = "failed"
#         return message
