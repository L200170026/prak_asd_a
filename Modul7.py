##JESSICA GUSTIN RAHAJENG/L200170026/A

import re

##no 1
a = open('Indonesia.txt', 'r')
teks = a.read()M
a.close()
x = r"me\w+"
hasil = re.findall(x, teks)
print(hasil)

##no2
a = open('Indonesia.txt', 'r')
teks = a.read()
a.close()
x = r"di\w+"
hasil = re.findall(x, teks)
print(hasil)

##no3
a = open('Indonesia.txt', 'r')
teks = a.read()
a.close()
x = r"di\s\w+"
hasil = re.findall(x, teks)
print(hasil)

##no 4a
f = open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
p4 = r'([\w+]+)</a></td>'
string = re.findall(p4,teks4)
print(string)

##no 4b
f = open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
string = re.findall(r'title="([\w+]+)">',teks4)
string = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)
