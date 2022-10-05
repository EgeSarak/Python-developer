
import re

string="search this inside of this text please!"


a=re.search("this",string)
print(a.span()) # indeks kaçtan kaça onu söyler.(17,21)
print(a.start()) #başlaıdıgı indexi verir
print(a.end()) #bittiği indexi verir
print(a.group()) #eşleşmenin(match) oldugu dizenin o parcasını veya bir kısmını verir



pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


a=pattern.search(string)
b=pattern.findall(string)
c=pattern.fullmatch(string)
d=pattern.match(string)
print(d)

string2="Andrei"
pattern2=re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password="hdjkahskdha5534%$9"
a=pattern.search(string2)
check=pattern2.fullmatch(password)
print(check)