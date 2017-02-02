#Author: Siladittya Manna

import urllib2,urlparse,os,sys
from bs4 import BeautifulSoup
download_path = '.....................' #Enter Download Path here
url='https://...............' #Enter URL of the page from which to download
page = urllib2.urlopen(url)
html = page.read()
i=0
#html.findall('.pdf')
soup = BeautifulSoup(html,'html.parser')
#print soup
links = soup.find_all('a',href=True)
for tag in links:
    tag['href']=urlparse.urljoin(url,tag['href'])
    if os.path.splitext(os.path.basename(tag['href']))[1]=='.pdf':
        current=urllib2.urlopen(tag['href'])
        print "\n[*]Downloading: %s" %(os.path.basename(tag['href']))
        f=open(download_path+'\\'+os.path.basename(tag['href']),"wb")
        f.write(current.read())
        f.close()
        i+=1
print "\n[*] Downloaded %d files" %(i+1)


