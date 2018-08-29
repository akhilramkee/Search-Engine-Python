from bs4 import BeautifulSoup
from urllib.request import urlopen

#Links to be crawled
linklist=['https://www.pdfdrive.com']

#Crawling process
for itr in linklist:
    
    print("Going into the link:" +itr)
    #Open the required url in the redditFile
    redditFile=urlopen(itr)
    redditHtml=redditFile.read()
    redditFile.close()
    
    soup=BeautifulSoup(redditHtml,features="lxml")
    redditAll=soup.find_all("a")
    for links in soup.select("a"):
        temp=links.get('href')
        temp1=itr+temp
        if temp1.endswith('pdf'):
            print("Pdf file:")
        else:
            if temp1.endswith('html'):
                linklist.append(temp1)
