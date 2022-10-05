# super() kullanım: üst sınıfa veya bu örnekte wizard ın üstündei sınıfa atıfta bulunur. Self e ihtiyac duyulmaz.

class User(object):
    def __init__(self,email):
        self.email = email
        
    def sign_in(self):
        print("logged in")
        
        
class Wizard(User):
    def __init__(self,name,power,email):
        super().__init__(email)
        #veya User.__init__(self,email)
        self.name = name
        self.power = power
        
    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")
        
        
wizard1= Wizard("Merlin",60,"merlin@gmail.com")
print(wizard1.email)        
            
                