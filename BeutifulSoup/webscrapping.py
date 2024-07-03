from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.div) #can use to access perticular tag
# print(soup.title.name) # to get tag name
# print(soup.title.string) # to get tag content
# print(soup.title.parent.name) 
# print(soup.find_all('div'))
# print(soup.find(id = 'header-container'))
# apply for all tag  

# for link in soup.find_all('a'):
#     print(link.get('href'))




 


