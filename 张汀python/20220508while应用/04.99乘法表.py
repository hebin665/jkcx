i =  1
while i < 10:
    j = 1
    while j < i+1:
        print(str(j)+"*"+str(i)+"="+str(i*j),end=" ")
        j+=1
    print()
    i+=1