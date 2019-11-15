import pdfkit
import urllib.request as urlreq
import re
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader, PdfFileWriter

filename = 'Introduction to Algorithms Cormen 3rd Edition.pdf'

outstream = open(filename,'wb')

url = "http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/toc.htm"

baseurl = "http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/"

website = urlreq.urlopen(url)

html = website.read().decode('utf-8')

#print(html)

soup = BeautifulSoup(html,features='lxml')

chaps2write = []

#pdfkit.from_url(prefaceurl,'preface.pdf')

for link in soup.findAll('a'):
	chapname = str(link.get('href'))
	chaps2write.append(chapname)
	pdfkit.from_url(baseurl+chapname,chapname[:-4]+'.pdf')

#https://stackoverflow.com/questions/3444645/merge-pdf-files

inpstream = []

for chapname in chaps2write:
	inpstream.append(open(chapname[:-4]+'.pdf','rb'))

writer = PdfFileWriter()

for reader in map(PdfFileReader,inpstream):
	for n in range(reader.getNumPages()):
		writer.addPage(reader.getPage(n))

writer.write(outstream)

for inps in inpstream:
	inps.close()


print('\n\n'+"Done.....We have the new book\n\n")
