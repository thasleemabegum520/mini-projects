sentence=input("enter characters of your choice:")
new_str=""

for x in range(len(sentence)):
    if sentence[x] in new_str:
        continue
    else:
        num=0
        for i in range(x,len(sentence)):
            if sentence[x] in sentence[i]:
                num+=1
        new_str=new_str+sentence[x]
    print(sentence[x],":",num,end=';')