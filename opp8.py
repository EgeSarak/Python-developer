# Multiple Inheritance

from sklearn.utils import check_array


class User():
    def sign_in(self):
        print("logged in")
        
class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power
        
    def attack(self):
        print(f"attacking with power of {self.power}")
        
class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows
        
    def check_arrows(self):
        print(f"{self.arrows} remaining")
        
    def run(self):
        print("ran really fast")
        
class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,arrows,):
        Archer.__init__(self,name,arrows)
        Wizard.__init__(self,name,power)
            
hb1 = HybridBorg("borgie",50,100)
print(hb1.attack())             
print(hb1.check_arrows())     
print(hb1.sign_in())    


print("******************************")

# MRO - Method Resolution Order
          
class A:
    num = 100
    
class B(A):
    pass

class C(A):
    num = 1             

class D(B,C):
    pass     

print(D.mro()) # sınıfın düzeni ya da Maro'sunu gösterir
#print(D.num)  
  
print("-----------------------------")

  
class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__) #veya print(M.mro())

  
                            
"""
    A
 /     \ 
/       \                        
B        C
\        /  
 \      /               
    D
    
"""    