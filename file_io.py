#my_file=open("test.txt")
"""
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())
"""
#satır okuma

#print(my_file.readline()) #1.satır
#print(my_file.readline()) #2.satır
#print(my_file.readline()) #3.satır

#print(my_file.readlines()) #bütün satırları okur.

#my_file.close() #dosyayı açtıktan sonra manuel olarak kapatmalıyız.

#dosya okuma
"""
with open("test.txt") as my_file:
    print(my_file.readlines())  """ #with open ile açtıgımızda manuel kapatmamıza gerek yok
    
    

#dosya yazma
"""
with open("test.txt",mode="r+") as my_file:
    text=my_file.write(':)')
    print(text)    """
    
#dosyanın sonuna ekleme
"""
with open("test.txt",mode="a") as my_file:
    text=my_file.write(':)')
    print(text)  """  
    
#yeni olusturma
with open("sad.txt",mode="w") as my_file:
    text=my_file.write(":(")
    print(text)    
    
#en yaygın kullanılanlar: okuma(r),yazma(w),ekleme(a)    