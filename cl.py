'''num = list(range(10,33))
list
print(num)
num2 = num[::-1]
print(num2)'''
import tkinter as TK
import turtle
my = turtle.Turtle()
my.speed(0)


def square(length, angle):
  my.forward(length)
  my.right(angle)
  
for i in range(200):
  square(200, 90)
  my.right(7)