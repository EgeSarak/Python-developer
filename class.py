# Object oriented programming (OOP)

#class

class Person:
    # class attributes
    address = "no information"
    # constructor (yapıcı metod)
    def __init__(self,name,year):
        #object attributes    
        self.name = name
        self.year = year
    
    #instance methods
    def intro(self):
        print("hello there. I am "+ self.name )
    #instance methods
    def CalculateAge(self):
        return 2022 - self.year        


#object (instance)
p1 = Person("ali",1990)
p2 = Person("yağmur",1995)

p1.intro()
p2.intro()

print(f"adım: {p1.name} ve yaşım: {p1.CalculateAge()}")
print(f"adım: {p2.name} ve yaşım: {p2.CalculateAge()}")


#updating
p1.name = "ahmet"
p1.address = "Kocaeli"
p2.year = 2000

# accessing object attributes
#print(f"p1 :name: {p1.name} year: {p1.year} address: {p1.address}")
#print(f"p2 :name: {p2.name} year: {p2.year} address: {p2.address}")


class Circle:
    # Class object attribute
    pi =3.14
    
    def __init__(self,yaricap = 1):
        self.yaricap = yaricap
        
    #methods
    def cevre_hesapla(self):
        return  2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return  self.pi * (self.yaricap ** 2)
    
c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f"c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")        
        