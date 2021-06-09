from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen('http://www.kastrup-genberg.se/') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
print(soup.title.string)