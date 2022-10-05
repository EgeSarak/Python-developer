is_old=True
is_licensed=True

if is_old and is_licensed:
    print("you are old enough to drive, and you have a licence!")   
else:
    print("you are not of age!")
    
print("okoko")        

username="johnny"
password="123"

if username and password:
    print("you are old enough to drive, and you have a licence!")   
else:
    print("you are not of age!")
    
print("okoko")  


#ternary operator

# condition_if_true if condition else condition_if_false

is_friend=True
can_message="message allowed" if is_friend else "not allowed to message"
print(can_message)

#short circuiting
is_Friend=False
is_User=True

if is_Friend or is_User:
    print("best friends forever")


is_magician=False
is_expert=True

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you are getting there")
else:
    print("you need magic powers")      
    
    
print(True==1)
print(''==1) 
print([]==1) 
print(10==10.0) 
print([]==[]) 

print(True is 1)
print('' is 1) 
print([] is 1) 
print(10 is 10.0) 
print([] is []) 

sayac=0
for i in (1,2,3,4,5):
    for j in (6,7,8,9,2):
        print(sayac,i,j)
        sayac+=1


user= {
    "name":"golem",
    "age":5006,
    "can_swim":False
}

for i in user.items():
    print(i)
    
for key,value in user.items():
    print(key,value)    
    
for i in user.keys():
    print(i)
    
for i in user.values():
    print(i)        
    
    

#counter
my_list=[1,2,3,4,5,6,7,8,9,10]

toplam=0
for i in my_list:
    toplam+=i
print(toplam)    

#range()
for i in range(0,10):
    print("email list")
    
for i in range(0,10,2):
    print(i)    
    
for i in range(10,0,-2):
    print(i)        
    
for i in range(2):
    print(list(range(10)))    #begendim iyi taktik
    
#enumerate()
for i,char in enumerate("hello"):
    print(i,char)    
    
for i,j in enumerate([1,2,3,4,5]):
    print(i,j)    
    
for i,num in enumerate(list(range(100))):
    if num == 50:
        print(f"index of 50 is : {i}")    

#while condition:
i=0        
while i <50:
    print(i)
    i+=1    
else:
    print("done with all the work")   
    
    
    
my_list=[1,2,3,5,6]
for i in my_list:
    print(i)
    
i=0
while i < len(my_list):
    print(my_list[i])
    i+=1             
    
    
"""while True:
    response = input("söyle: ")
    if(response == "bye"):
        break   """
    
#exercise
picture=[
    [0,0,0,1,0,0,0],     
    [0,0,1,1,1,0,0],     
    [0,1,1,1,1,1,0],     
    [1,1,1,1,1,1,1],     
    [0,0,0,1,0,0,0],     
    [0,0,0,1,0,0,0]]

for row in picture:
    for pixel in row:
        if pixel==1:
            print("*",end='')     
        else:
            print(' ',end='')    
    print('')            
    
some_lsit=["a","b","c","b","d","m","n","n"]
    
duplicates=[]
for i in some_lsit:
    if some_lsit.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)        
        
#functions

def say_hello():
    print("helloo")

say_hello() 


def tree():
    for row in picture:
        for pixel in row:
            if pixel==1:
                print("*",end='')     
            else:
             print(' ',end='')    
        print('')            
    
    
tree()   
tree()

#parameters
#default parameters
def say_hello(name="vader",emoji=":("):
    print(f"helloo {name} {emoji}")
    
#positional arguments
say_hello("Ege",":)")    
say_hello("Mehmet",":)")    
say_hello("Engin",":)")    

#keywords arguments
say_hello()
say_hello("Ege",":)")    
say_hello("Ege")    


#return
def sum1(num1,num2):
    return num1+num2

print(sum1(3,4))

total=sum1(10,5)
print(sum1(10,total))


def sum1(num1,num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func(num1,num2)

total1=sum1(10,20)
print(total1)


def carp(n1,n2):
    def other(num1,num2):
        return num1 * num2
    return other(n1,n2)

print(carp(5,7))

#docstrings

def test(a):
    """
    info: this fucntipn tests and prints param a
    """
    print(a)
    
print(test.__doc__)

#clean code 
def is_even(num):
    return num % 2 == 0

    
print(is_even(5))       


# *args  **kwargs

def super_func(*args,**kwargs):
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args) + total

print(super_func(1,2,3,4,5,6,7,8,9,num1=5,num2=10))

#rule : params, *args, default parameters, **kwargs
#örneğin

##  def func(name,*args,cumle="hi",**kwargs)

#exercise
def highest_even(li):
    evens=[]
    for i in li:
        if i % 2==0:
            evens.append(i)
    return max(evens)            

print(highest_even([10,2,3,4,8,11]))
    
