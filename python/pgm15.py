s = input(" enter a sentence :")
l=d=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("the number of letters are :",l)
print("the number of digits are :",d)