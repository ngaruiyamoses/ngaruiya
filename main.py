####
#   Name : Moses Ngaruiya
#   Date  : 6th June 2022
##########
import operation
#from student import student

from teachers import Teachers

print(operation.div_numbers(9,3))
print(operation.mult_numbers(34,68))
print(operation.sub_numbers(67,96))
print(operation.add_numbers(43,95))



#new_student = student("moses" , "swimming" , "1824")
#print(student.greet_student())

new_teacher = Teachers("Mr Mwangi",126474,"Biology",70000)
print(new_teacher.get_tsc_no())