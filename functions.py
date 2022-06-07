###functions is a block of code which gets executed together

#################
#functions in python
#    name: Moses Ngaruiya
#    date: 31\5\22

def say_hello():
    #print("Hello from JKUAT")

    x = 7 
    y = 8
    z = x+y 
    #print(z)
say_hello()   

def bark():
    #print("dogs bark goof goof goof")
    #print("cow moos moo moo moo")
    #print("duck quacks quack quack")
#bark()    

###functions parameters
def add_numbers (x,y):
    sum_nums = x+y
    #7print("the sum of numbers:",sum_nums)
add_numbers (68,89)   
add_numbers (78,90)
add_numbers (45,64) 

def multiply_numbers (x,y):
    prod_nums = x*y
    #print("the product of numbers:",prod_nums)
multiply_numbers (67,34)
multiply_numbers (80,70) 

#calling the function
import math 

a = int(input("enter the coefficient of the first term"))
b = int(input("enter the coefficient of the second term"))
c = int(input("enter the constant"))
w = math.sqrt((b**2)-4*a*c)

def find_roots (a,b,c):
    y_1 = ((-b + w)/(2*a))
    y_2 = ((-b - w)/(2*a))
    #print("the roots of equation are:",y_1,y_2)
find_roots (a,b,c)    

def print_name(name = "Moses Ngaruiya"):
    print(name)
print_name("John")    