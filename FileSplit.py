import re
with open('/Users/adam/Desktop/Atom/file.txt','r+') as f1:
	for lines in f1:
		if "@" in lines:
			r1=re.compile(r'(\S+@\S+.[A-Za-z]{2,4})')
			result=r1.findall(lines)
			for email in result:
				replace=email.split("@")[0]
				f2=lines.replace(replace,"replace")
				f1.write(f2)
		else:
			continue

