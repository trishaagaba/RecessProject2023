# git config --global user.name 'AgabaTrisha'
# git config --global user.email 'aggab'
# import requests - fetches the html content

# url https://xeno-canto.org

from bs4 import BeautifulSoup
import requests

url= 'https://xeno-canto.org'
response= requests.get(url)

# Get title of the website
soup= BeautifulSoup(response.content, 'html.parser')

title= soup.find('title')
print(title)





