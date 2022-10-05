def hello(func):
    func()
    
def greet():
    print("still here !")
    
a=hello(greet) 
print(a)   

#hight order function HOC

def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func 

#decorator
"""def my_decorator(func):
    def wrap_func():
        print("******")
        func()
        print("******")
    return wrap_func"""

#1.yol
"""@my_decorator
def hello():
    print("hello")
    
@my_decorator   
def bye():
    print("see ya later")    
    
hello()    
bye()        """


#2.yol
"""def hello():
    print("hello")
    
def bye():
    print("see youu")      

    
hello2=my_decorator(hello) 
hello2()      

bye2=my_decorator(bye)
bye2()
"""
#---------------------
#decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("******")
        func(*args, **kwargs)
        print("******")
    return wrap_func



@my_decorator
def hello(greeting,emoji=":("):
    print(greeting,emoji)
    
#hello("hiii")    

#veya
"""a=my_decorator(hello)
hello("hiiii",":)")"""

hello("hiii")

#ne kadar sürede çalıştığını söyleyen decorator
from time import time
def performance(fn):
    def wrapper(*args,**kwargs):
        t1=time()
        result=fn(*args,**kwargs)
        t2=time()
        print(f"took {t2-t1} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000):
        i*5

long_time()        