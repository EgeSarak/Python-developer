#error handling

while True:
    try:
        age=int(input("what is your age ?"))
        print(age)
    except :
         print("please enter a number")  
    else:
        print("thank you")
        break      
        
      
while True:
    try:
        age=int(input("what is your age ?"))
        10/age
    except ValueError:
         print("please enter a number")  
    except ZeroDivisionError:
         print("please enter age higher than 0")  
    else:
        print("thank you")
        break         
        
       
def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"please enter numbers {err}") 
        
print(sum(1,'2'))                 


       
def sum(num1,num2):
    try:
        return num1 + num2
    except (TypeError,ZeroDivisionError) as err:
        print(err)
        print("oopps") 
        
print(sum(1,'2'))              




while True:
    try:
        age=int(input("what is your age ?"))
        10/age
    except ValueError:
         print("please enter a number")  
         continue
    except ZeroDivisionError:
         print("please enter age higher than 0")  
         break
    else:
        print("thank you")
        break
    finally:
        print("ok,i am finally done")
    print("can you hear me ?")        
  
  
 
while True:
    try:
        age=int(input("what is your age ?"))
        10/age
    except ValueError:
         print("please enter a number")  
         continue
    except ZeroDivisionError:
         print("please enter age higher than 0")  
         break
    else:
        print("thank you")
    finally:
        print("ok,i am finally done")
    print("can you hear me ?")      
    
    
while True:
    try:
        age=int(input("what is your age ?"))
        10/age 
        raise Exception("hey cut it out")
    except ZeroDivisionError:
         print("please enter age higher than 0")  
         break
    else:
        print("thank you")
    finally:
        print("ok,i am finally done")
    print("can you hear me ?")   