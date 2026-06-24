str=input("enter a word:")
rev_str=""
for x in range(len(str)):
    rev_str=rev_str+str[len(str)-x-1]
print("Reverse of ",str,"is",rev_str)
if str==rev_str:
    print("Yes it is a palindrome")
else:
    print("its is not a palindrome")



