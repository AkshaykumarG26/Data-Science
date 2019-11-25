# Even or Odd

num1 = int(input("Enter a Number: "))
mod = num1 % 2
if mod > 0:
    print("GIven number is Odd")
else:
    print("GIven number is Even")



# Prime or not

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")