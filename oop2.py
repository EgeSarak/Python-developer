# classmethod and staticmethod

class PlayerCharacter:
    membership = True
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def shout(self):
        print(f"my name is {self.name}")
        
    #decarator
    @classmethod # çok kullanmayız
    def adding_things(cls,num1,num2):
        return cls("Teddy",num1 + num2) #5 yasında olması gereken teddy adında nesne olusturdum.
       #classmethod ile yeni bir oyuncu olusturmus oldum.    
    
    @staticmethod #cok kullanılmaz (sınıfa erişimimiz yoktur)
    def adding_things2(num1,num2):
        return num1 + num2        

player1=PlayerCharacter("Tom",20)
print(player1.shout())      
#print(player1.adding_things(2,3))  
player3 = PlayerCharacter.adding_things(2,3)
print(player3.name)    
print(player3.age)    