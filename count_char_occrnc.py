str=input("enter characters of your choice:")
new_str=""

for x in range(len(str)):
    if str[x] in new_str:
        continue
    else:
        num=0
        for i in range(x,len(str)):
            if str[x] in str[i]:
                num+=1
        new_str=new_str+str[x]
    print(str[x],":",num,end=';')