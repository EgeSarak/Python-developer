class Cat:
    species = "mammal"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
#1) Instantiate the cat object with 3 cats   

peanut = Cat("peanut",3)
garfield = Cat("garfield",5)
snickers = Cat("snickers",6)

#2)Create a function that finds the oldest cat

def get_oldest_cat(*args):
    return max(args)

#3) Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2     

print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")