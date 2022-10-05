# polymorphism

class User():
    def sign_in(self):
        print("logged in")
        
    def attack(self):
        print("do nothing")    
        
class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")
    
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows 
        
    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")   
        
        
wizard1 = Wizard("Merlin",50)
archer1 = Archer("Robin",30)
print(wizard1.attack()) #do nothing de yazdı
print(archer1.attack()) #yazmadı.Cunku User.attack(self) Archer sınıfına koymadım.

#1.yol
""" 
def player_attack(char):
    char.attack()
    
player_attack(wizard1)
player_attack(archer1)  """

#2.yol
"""for char in [wizard1,archer1]:
    char.attack()"""
  
    
    


    
      
