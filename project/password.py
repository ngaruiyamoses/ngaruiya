import random
print('welcome to our project generator')
character = str("Moses Ngaruiya")
num_pass = int(input("enter number of password you would like to generate:"))
len_pass = int(input("length of password:"))

print(" \n here are your passwords : ")
for password in range(int(num_pass)):
    password= " "
    for c in range(int(len_pass)):
        password += random.choice(character)
    print(password)    
