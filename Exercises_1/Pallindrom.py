txt = input("Enter a String: ")

if txt[0:] == txt[::-1]:
    print ("entered string is pallindrom: ",txt)
else:
    print ("entered string is not pallindrom: ",txt)