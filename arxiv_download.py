import os,arxiv

query_string = input("Enter Query: ")
cwd = os.getcwd()
print(cwd)
new_path = cwd+"/"+query_string
'''if not os.path.exists(new_path):
    os.makedirs(new_path)
download_path = new_path'''
#os.chdir(new_path)
print("Getting papers...")
results = arxiv.query(query=query_string,max_results=10000)
print(len(results)," papers retrieved...")

query_words = query_string.lower().split(' ')
papers = []
for r in results:
	if all(word in r['title'].lower().split(" ") for word in query_words):
		papers.append({'pdf_url':r['pdf_url'],'title':r['title']})

print(len(papers)," papers filtered...")
'''for p in papers:
	print("Downloading : "+p['title']+"\n")
	try:
		arxiv.download(p,dirpath=download_path,prefer_source_tarfile=False)
	except:
		print("Download Failed!!!")
'''