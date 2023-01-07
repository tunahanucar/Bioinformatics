f = open("file.txt",'r')

cont = f.readlines()

for i in range(0,len(cont)):
    if(i % 2 == 1):
        print(cont[i])
    else:
        pass

