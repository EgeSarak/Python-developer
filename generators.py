
print(range(0,100))
print(list(range(100)))

def make_list(num):
    result=[]
    for i in range(num):
        result.append(i*2)
    return result    

print(make_list(10))


def generator_function(num):
    for i in range(num):
        yield i*2 #yield: işlevi duraklatır ve sonra ki çağrıldığında ona geri döner

g=generator_function(100)
next(g) #0
next(g) #2
next(g) #4
next(g) #6
next(g) #8
print(next(g)) #10     


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
    print("1")
    for i in range(100000):
        i*5

long_time()          


@performance
def long_time2():
    print("2")
    for i in list(range(100000)):
        i*5

long_time()  
long_time2()   

def generator_func(num):
    for i in range(num):
        yield i

for item in generator_func(100):
    print(item)        
    
    
def special_for(iterable):
    iterator=iter(iterable)
    while True:
        try:
            print(iterator)
            # next(iterator) # yinelenebilir nesneler arasında döngü yaptırıyor
            print(next(iterator)*2) #hem nesneleri hem değerleri yazdırdım.
        except StopIteration:
            break

special_for([1,2,3])      


#exercise fibonacci

def fib(number):
    a=0
    b=1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b        
        
for x in fib(20):
    print(x)         
    
    
def fib2(number):
    a=0
    b=1
    result=[]
    for i in range(number):
        result.append(a)
        temp=a
        a = b
        b= temp + b
    return result 

print(fib2(10))                  
 

