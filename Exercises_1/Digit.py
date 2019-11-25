str1 = input("Enter a string: ")
d=l=0
for i in str1:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        l += 1
    else:
        pass
print("Digits: ", d)
print("Letters: ", l)