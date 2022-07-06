print(5+8)
print(6*9) 
day=7
print(day + 6)
day = 7
month = "February"
dayName = "Friday"
temp = 26
print(f"today is {dayName} {month} {day} and its {temp} degrees outside")

phoneIsCharging = False
if phoneIsCharging:
    print("charging")

age = 30
if age >= 18:
    print("you're an adult")
else:
    print("you're a child")

import random
print(random.randint(1,30))
print(random.random())

luckyNumber = random.randint(1,100)
fortuneNumber = random.randint(1,3)

if fortuneNumber ==1:
    fortuneText="you will have a great day"
if fortuneNumber ==2:
    fortuneText = "you will live to 100"
if fortuneNumber ==3:
    fortuneText = "you are great"   
print(f"{fortuneText} and your lucky number is: {luckyNumber}")

fav_numbers = [7,77,777]
fav_numbers.append("7777")
fav_numbers.insert(0,88)
del fav_numbers[2]
print(len(fav_numbers))
#del(fav_numbers[0])
#del(fav_numbers[1])
#del(fav_numbers[1])

for number in fav_numbers:
    print(number)
print(fav_numbers)

for number in range(40):
    print((number+1)*2)


dogs = {7:"tarzan", 8:"simba", 3:"puppy"}
print(dogs[7])
dogs[9]="puma"
print(dogs)