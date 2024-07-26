import requests
from bs4 import BeautifulSoup
import pandas as pd

books=[]
count=0
try:
    for i in range(1,51):
        source =  requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
        source.raise_for_status()
        soup = BeautifulSoup(source.text,'html.parser')
        ol=soup.find("ol")
        articles =  ol.find_all('article',class_="product_pod")
        for article in articles:
            image=article.find('img')
            title=image.attrs['alt']
            star=article.find('p')
            star="RATING : "+star['class'][1]+" Star"
            price= article.find('p',class_="price_color").text
            price=float(price[2:])
            books.append([title,star, price])
            #print(title)
        print("Fetching All The Titles..........")
        for book in books:
            print(book)
            count=count+1
        print("Total Books Fetched......."+str(count))
    df = pd.DataFrame(books,columns=['Title','Star','Price'])
    df.to_csv("Books.csv")
except Exception as e:
    print("THE EXPECTION IS ............"+ str(e))

