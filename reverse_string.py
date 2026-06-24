str=input("enter a word:")
rev_str=""
for x in range(len(str)):
    rev_str=rev_str+str[len(str)-x-1]
print(rev_str)



