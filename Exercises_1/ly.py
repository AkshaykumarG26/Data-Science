str1 = input("Enter a String: ")
length = len(str1)

if length > 2:
    if str1[-3:] == 'ing':
        str1 += 'ly'
        print(str1)
    else:
        str1 += 'ing'
        print(str1)