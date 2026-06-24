x=["a",1,2,3,4,5,3,2,"a","b"]
y=set(x)

b=list(y)
for i in range(len(b)):
    num=0
    for j in range(len(x)):
        if b[i]==x[j]:
            num+=1
    print(b[i],":",num)


