###
def print_name(name = "Moses Ngaruiya"):
    print(name)
print_name("John")    

#return from a function
def get_sum(num1 , num2):
    sum_nums = num1 + num2
    return sum_nums
print(get_sum(5,83))

##function to get square of numbers
def powers(number , power):
    pow_num = number**power
    return pow_num
print(powers(5,6))     

def get_full_name(f_name , s_name):
    full_name = f_name + " " + s_name
    return full_name
print(get_full_name("Moses" , "Ngaruiya"))

####returning a dictionary from a function
def create_full_name(first_name , second_name):
    person = {'first':first_name, 'second':second_name}
    return person
student = create_full_name('Moses' , 'Ngaruiya')
print(student)

###parsing a list in a function
def greet_friends(names):
    for name in names:
        msg = "hello " + name.title() + "!"
        print(msg)
friends = ['John' , 'Malcom' , 'Lenny' , 'George']
greet_friends(friends)

