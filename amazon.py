import amazonscraper
from bs4 import BeautifulSoup
import urllib.request
results=amazonscraper.search("Python Programming",max_product_nb=2)
for result in results:
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    url='https://www.amazon.com/dp/'+result.asin
    request= urllib.request.Request(url,headers={'User-Agent': user_agent})
    html=urllib.request.urlopen(request)
    soup=BeautifulSoup(html,'lxml')
    price=soup.findAll('span',attrs={'id':'priceblock_ourprice'})
    p=BeautifulSoup(str(price),'lxml')
    print(p.text)
