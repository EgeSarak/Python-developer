#Data Types

print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2/4))

print(round(3.1))
print(round(3.9))

print(abs(-20))

a,b,c=1,2,3
print(a)
print(b)
print(c)


isim="ege"
soyad="sarak"

print(isim+soyad)
print(isim,soyad)
print(isim + " " + soyad)

print("hello" * 5)

print(type(int(str(100))))

a=str(100)
b=int(a)
c=type(b)
print(c)

weather="It's 'kind of' sunny"
weather2="It's\n 'kind of'\n sunny"
print(weather)

name="Johnny"
age=55

print("hi " + name + ". You are " + str(age) + " year old")
print(f"hi {name} . You are {age} year old.") #favorim
print("hi {}. You are {} years old".format(name,age))
print("hi {1}. You are {0} years old".format(name,age))

print("hi {new_name}. You are {new_age} years old".format(new_name="ege",new_age=40))

selfish="me me me"
        #01234567
        
print(selfish[0])
print(selfish[2])        
print(selfish[7])

#[start:stop:stepover]
selfish2="01234567"
print(selfish2[0:8:2])        
print(selfish2[1:])   
print(selfish2[:5])    
print(selfish2[::1])     
print(selfish2[::-1])      
print(selfish2[::-2])        

selfish2+="8"
print(selfish2)

greet="hellloooo"
print(len(greet))
print(greet[:])
print(greet[0:len(greet)])

quote="to be or nor to be"

print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find("be"))
quote2=quote.replace("be","me")
print(quote)
print(quote2)

#yas tahmin etme
"""
birth_year=int(input("what year were ypu born ?"))
age=2022-birth_year
print("yaşınız: ",age) """

list11=[1,2,3,4,5]
l2=["a","b","c"]
l3=[1,2,"a",True]

amazon_cart=["notebooks","sunglasses"]
print(amazon_cart[0])
print(amazon_cart[1])

amazon_cart2=["notebooks","sunglasses","toys","grapes"]

print(amazon_cart2[0:2])

amazon_cart2[0]="laptop"
new_cart=amazon_cart2[:]
new_cart[0]="gum"
print(amazon_cart2)
print(new_cart)

#matrix
matrix=[[1,2,3],
        [2,4,6],
        [7,8,9]
    ]

print(matrix[0][2])

basket=[1,2,3,4,5]
print(len(basket))

basket.append(100)
new_list11=basket
print(basket)
print(new_list11)

basket.insert(4,200)
new_list1=basket
print(basket)
print(new_list1) 

basket.extend([100,101])
new_list1=basket
print(basket)
print(new_list1)

basket.pop()
basket.pop()
basket.pop(0)
print(basket)

basket.remove(200)
basket.remove(4)
print(basket)


new_list1=basket.pop(2)
print(new_list1)

new_list1=basket.clear()
print(new_list1)
print(basket)


basket2=["a","b","c","d","e","d"]
print(basket2.index("d"))  
print("d" in basket2)
print("x" in basket2)

print(basket2.count("d"))
basket2.sort()
basket2.reverse()
print(basket2)
    

new_sentence=" ".join(["hi","my","name","is","JOJO"])    
print(new_sentence) 

#list1 unpacking        
a,b,c,*other,d=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)  
print(c)  
print(other)  
print(d)

weapons=None
print(weapons)

#dictionary

dict1={"a":1,"b":2,"c":3}
print(dict)

"""for i,j in dict.items():
        print(i,j)"""
        
print(dict["b"])        

dict2={"a":[1,2,3],"b":"hello","x":True}

print(dict2["a"][2])
print(dict2["b"])
print(dict2["x"])

my_list1=[{"a":[1,2,3],"b":"hello","x":True},
         {"a":[4,5,6],"b":"hello","x":True}]

print(my_list1[0]["a"][2])

user={"basket":[1,2,3],"greet":"hello","age":20}
print(user.get("age",55)) #55 default deger olarak verdim


user2={"isim":"ege",
       "soyad":"sarak",
       "yas":25,
       "boy":178,
       "araba":"renault",
       }

print(user2.get("iş","data science"))


user3=dict(job="data sicence") #2. sözlük olusturma yöntemi
print(user3)


sayac=0
for i,j in user2.items():
        print(sayac,i,j)
        sayac+=1
        
        
print("basket" in user)   
print("greet" in user.keys())   
print("hello" in user.values())   

print(user.items())

#print(user.pop("age"))
#print(user)

print(user.popitem())
print(user)

print(user.update({"age":55}))
print(user)

#tuple

my_tuple=(1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

user5={
     (1,2):[1,2,3,],
     "greet":"hello",
     "age":20           
}


print(user5[(1,2)])

new_tuple=my_tuple[1:4]
print(new_tuple)

x,y,z,*other=(1,2,3,4,5,6,7,8,9)
print(x)
print(y)
print(z)
print(other)


#count
print(my_tuple.count(5)) # 5 ten kaç tane oldugunu söyledi
#index
print(my_tuple.index(3)) # 3 ün kaçıncı indekste oldugunu söyledi
#len
print(len(my_tuple)) #uzunlugu,kaç elemanı oldugunu söyler

#sets(kümeler) : unique(eşsiz) degerleri döndürür

my_set={1,2,3,4,5,5} 
my_set.add(100)
my_set.add(2) #2 zaten kümemizde oldugu için eklenmedi
print(my_set)

my_list12=[1,2,3,4,5,5]
set=set(my_list12)
print(set)


my_set3={1,2,3,4,5,5} 
new_set=my_set3.copy()
print(list(new_set))
print(my_set3)

#set fonksiyonları
"""
.difference(): iki küme arasında ki farklı olanları yazdırır
.discard(): eleman çıkartmak için
.difference_update(): iki kümede olan yani aynı elemanları çıkartır
.intersection() : kesişimleri verir.aynı olanları
.isdisjoint() : iki kümede aynı degerler varsa true ,yoksa false döner.yani ortak nokta var mı yok mu ona bakıyoruz.
.issubset() : alt küme
.issuperset() : üst küme
.union() : iki kümeyi birleştirir.ve aynı değerleri tekrar etmez.
"""

my_set={1,2,3,4,5}
your_set={4,5,6,7,8,9,10}

print(my_set.difference(your_set))
print(my_set.discard(5)) # 5 i çıkarttık
print(my_set.difference_update(your_set)) 
print(my_set)

print(my_set.intersection(your_set)) 

