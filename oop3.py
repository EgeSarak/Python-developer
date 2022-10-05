#private : Pythonda böyle bir özellik olmadıgından alt çizgi örn:(_name,_age) olarak kullanılır.
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    def run(self):
        print("run")
        
    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old")

player1=PlayerCharacter("andrei",100)
player1.name ="!!!"
player1.speak= "BOOOOO"

print(player1.speak)

                    