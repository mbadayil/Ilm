import re
r=re.compile(r'(\d{3}-\d{3}-\d{4})')
with open('/Users/adam/Desktop/Atom/file.txt','r') as f1:
    with open('/Users/adam/Desktop/Atom/file_copy.txt','w') as f2:
        for line in f1:
            phone=re.findall(r'[\w\.-]+@[\w\.-]+\.\w{3}',line)
            if ''.join(phone) in line:
            #    print(phone
                #f2.write(''.join(phone).replace('408','786'))
                print(phone)



#((?:\d{3})-(?:\d{3})-(?:\d{4}))
