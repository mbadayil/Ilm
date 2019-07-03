import re
with open('/Users/adam/Desktop/Atom/file.txt','r') as f1:
	chunk_size=100
	content=f1.read(chunk_size)
	while len(content)>0:

		print("***",content)
		print(f1.tell())
		content=f1.read(chunk_size)









"""
r=re.compile(r'(\(?\d{3}\)?-\d{3}-\d{4})')
#r1=re.compile(r'(\S+@\S+.[A-Za-z]{2,4})')
r1=re.compile(r'(\S+@\S+.[A-Za-z]{2,4})')

result=r.findall(read1)
result1=r1.findall(read1)
#print(result)
"""
