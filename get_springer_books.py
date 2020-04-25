import re, progressbar, requests
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer

df = pd.read_excel(r"Springer Ebooks.xlsx", header=1)
books = [(unicode(x).encode('UTF8'), y, unicode(z).encode('UTF8')) for x, y, z in zip(df['Book Title'], df['OpenURL'],df['Author'])]
bar = progressbar.ProgressBar(maxval=len(books)).start()
index = 0

try:
        
    for index, book in enumerate(books):
        url = requests.head(book[1], allow_redirects=True).url
        url = url.replace("book", "content/pdf") + ".pdf"
        
        response = requests.get(url)
        with open("./books/" + ''.join(ch for ch in book[0] if ch.isalnum() or ch == ' ') + " by " 
        + ''.join(ch for ch in book[2] if ch.isalnum() or ch == ' ') +".pdf", 'wb') as f:
            f.write(response.content) 
        
        print(index,book[0], book[2])
        bar.update(index)
        
        

except:
    print("Download unsuccessful")

if index == len(books) - 1: print("Downloading " + str(len(books)) + " books complete")