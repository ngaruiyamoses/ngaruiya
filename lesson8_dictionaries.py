

#############
#   Dictionaries
#   Name : Moses Ngaruiya
#   Date  : 
##########

#Initializing dictionaries
student={"name" : "Moses", "age" : "20", "gender" : "male"}
print(student["name"])
print(student["age"])
print(student["gender"])

#Adding key values in a dictionary
student["id"]="5789"
student["hobby"]="swimming"
student["club"]="chui"
print(student)
 
 #empty dictionary
#student={}
student["fav_food"]="chapati"
student["home_city"]="kikuyu"
print(student)

#modifying values
student["Name"]="John"
print(student)

for number in range(0,9):
    #7print(number)
    print(number**2)
    print("number\tsquare")
    print("==============")



h=eval(input("9"))
for x in range(h):
    print("" * (h - x),"*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print("" * (h - x), "*" * (2*x + 1))
