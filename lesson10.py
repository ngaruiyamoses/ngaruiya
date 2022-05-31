#####
#print(range (0,29))
for numbers in range(0,10):
    #print(numbers)
    #print(numbers %2)
    if(numbers %2==0):
        #print(numbers)

#sum of all even numbers btn (0,50)
sum_nums = 0
for numbers in range(0,50):
    if(numbers %2==0):
        sum_nums = sum_nums + numbers
        #print(sum_nums)

#product of odd numbers btn (0,20)
prod_nums = 1
for number in range(0,20):
    if(number %2==1):
        prod_nums = prod_nums * number

#print(prod_nums) 

#####
num = 10
while num <10:
    if(num %2==o):
        #print(num)
        num = num + 1


######Write a program to check if a number is divisible by 5 or 7
number = user.input("enter a number")
if(number %7==0) and (number %5==0):
    print("it is divisible by 7 or 5")
else:
    print("it is not divisible by 7 or 5")    


