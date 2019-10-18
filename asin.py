from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'https://www.amazon.in/IN2-Whey-Protein-Mango-500/dp/B07JMXT3S7/ref=sr_1_2_sspa?crid=3C28RM2N3BUD2&keywords=whey+protein+1kg&qid=1568384501&s=gateway&sprefix=whey+pr%2Caps%2C1038&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUFpSOFlQUlQ0VExGJmVuY3J5cHRlZElkPUEwMDExMjMzVk0zRUdMMTlHWERNJmVuY3J5cHRlZEFkSWQ9QTA0MzM1MDIzMkVTSEs3V01DMjdGJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
tag = soup.find('div',attrs={'id':'cerberus-data-metrics'})
asin= tag.get('data-asin')
print(asin)