import math
try:
    num=int(input("enter a number:"))       
    if num<0:
        raise ValueError("Negative number....")
except ValueError:
    print("enter positive number only....")    
else:
    print("squareroot:", round(math.sqrt(num),4))    