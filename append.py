with open("log.txt", 'a+') as f:
    f.write("nine")
    f.seek(0)
    data=f.read()
    print("current data:\n",data)