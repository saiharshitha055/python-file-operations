import math
try:
    num=int(input("enter a number:"))
    print(num)
    raise ValueError
except:
    print("Exception raised intentionally even no use....")
    