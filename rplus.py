with open("file1.txt", 'w+') as f:
    f.write("Hello Students!!!")
    f.seek(0)
    data=f.read()
    print("Previous:", data)
    new_data=data.replace("Students!!!","Future IT Employees")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("file1.txt", 'w') as f:
    f.write("sai harshitha")
with open("file1.txt", 'r+') as f:
    data=f.read()    
    print("Previous:", data)
    new_data=data.replace("sai", "kolluri")
    f.seek(10)
    f.write(new_data)
    f.truncate(2)
with open("file1.txt", 'r')  as f:
    print("latest:", f.read())   