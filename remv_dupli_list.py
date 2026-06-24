lis=["a",12,23,21,65,65,67,67]
new_lis=[]

for i in range(len(lis)):

    if lis[i] not in new_lis:

        new_lis.append(lis[i])
    else:
        continue
print(new_lis)

