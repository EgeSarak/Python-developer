#OPP
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self,name = "anonymous",age = 0):
        if (PlayerCharacter.membership):
            if (age > 18):
                self.name = name # attributes
                self.age = age
        
    def shout(self):
        print(f"my name is {self.name}")
        
    def run(self,hello):
        print(f"my name is {self.name}")        
        
        
player1= PlayerCharacter("Cindy",44)   
player2= PlayerCharacter("Tom",21)   
player2.attack= 50

print(player1.name,player2.name)       
print(player1.age,player2.age)   
print(player2.attack)    
  

#help(player1) # nesnenin tüm planını verir
# help(list) #python veri türlerinin hangi sınıf planına sahip olduğunu görmek için

print(player1.shout())
print(player2.shout())
print(player1.run("hello"))


player3=PlayerCharacter("Jack",20) # yaşı 18 den küçük olunca hata verir.
print(player3.shout())

