def sayilar(li):
    square=[]
    for i in li:
        square.append(i*2)
    return square            
           
print(sayilar([1,2,3]))    


#map,filter,zip and reduce

#map
my_list=[1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2,my_list)))
print(my_list)

listem=["ege","ahmet","fatih"]
def uppercase(a):
    return a.upper()

print(list(map(uppercase,listem)))
            
#filter

def only_odd(x):
    return x % 2 ==1

print(list(filter(only_odd,my_list)))
print(my_list)

#zip

list1=["a","b","c"]
list2=[10,20,30]
list3=[5,4,3]

print(list(zip(list1,list2,list3)))

isimler=["ege sarak","engin solmazgul","mehmet sait","corc lukas"]
postalar=["egesarak@gmail.com","engin@gmail.com","mehmet@gmail.com","corc@gmail.com"]
numaralar=[1236544565,4567542343,1123456733,1234567654]
notlar=["ff","aa","bb","aa"]

for i in zip(isimler,postalar,numaralar,notlar):
    print("bilgiler: ",i)

#reduce
from functools import reduce

def accumulator(acc,item):
    print(acc,item)
    return acc + item

print(reduce(accumulator,my_list,0)) #(fonksiyon,listem,acc default degeri)
print(reduce(accumulator,my_list,10)) #(fonksiyon,listem,acc default degeri)


#exercise
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def makeCaps(word):
  return(word.capitalize())
  
print(list(map(makeCaps,my_pets)))

scores = [73, 20, 65, 19, 76, 100, 88]

def checkPass(score):
  return score > 50

print(list(filter(checkPass,scores)))

my_numbers = [5,4,3,2,1]
def combineNums(startValue,number):
  print(startValue,number)  
  return startValue + number
  
print(reduce(combineNums, my_numbers + scores, 0))


#lambda expressions lambda param: action(param)

print(list(map(lambda x : x * 2,my_list)))

print(list(filter(lambda x : x > 1,my_list)))

print(reduce(lambda x,y : x + y,my_list))

#-------------------------------------------    
my_list2=[5,4,3]
#square
new_list=list(map(lambda x :x**2,my_list2)) 
print(new_list)

#list sorting
a=[(0,2),(4,3),(9,9),(10,-1)]    
print(a.sort(key=lambda x: x[1])) 
print(a)


#list comprehensions # list=[param for param in iterable]
my_list3=[]

for char in "hello":
    my_list3.append(char)
print(my_list3)    
    
    
my_list4=[char for char in "hello"] 
print(my_list4)   

my_list5=[i for i in range(0,10)]
print(my_list5)

my_list6=[i*2 for i in range(0,10)]
print(my_list6)
 
my_list7=[i for i in range(0,10) if i%2== 0]    
print(my_list7)

#dict
simple_dict={
    "a":1,
    "b":2
}

my_dict={key:value**2 for key,value in simple_dict.items()}
print(my_dict)

my_dict2={k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict2)

my_dict3={num:num*2 for num in [1,2,3]}
print(my_dict3)

#exercises

some_list=["a","b","c","b","d","m","n","n"]

duplicates=list(set([i for i in some_list if some_list.count(i) > 1 ]))
print(duplicates)


orn=[1 if i %2 ==0 else 0 for i in range(20)]
print(orn)