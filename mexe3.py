import datetime
try:
    x=int(input("enter numerator:"))
    y=int(input("enter a denominator:"))
    print("result:",x/y)
except Exception as e:
    ct=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")    
    txt=f"[{ct}] Error:{str(e)} \n"
    with open("data.txt",'a') as file:
        file.write(txt)