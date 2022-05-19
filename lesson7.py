#learning about a list
motorcycle_owner = "moses ngaruiya"
plate_number = ["H234", "S345", "Y960"]
motorcycle = ["Honda","Suzuki","Yamaha"]
print(motorcycle)
print(plate_number)
print(motorcycle_owner)

#accessing list using git index
# motorcycle[3]= "Bugatti"#changing element in a list
#print("i love" + motorcycle[1])
#adding element to list
#motorcycle .append("Bugatti ") #adding an item to list --append
print(motorcycle[0] ,plate_number[0] ,motorcycle[1] , plate_number[1] , motorcycle[2] , plate_number[2])
#deleting an item from a list --delete
#del motorcycle[2] #deleting an item from a list
#popped_motorcycle = motorcycle.popp()
#print(popped_motorcycle)
#print a statement
print( "My name is " + motorcycle_owner + " and i own " + motorcycle[0] + plate_number[0])
print(f"My name is {motorcycle_owner} and i own {motorcycle[0]} ,{plate_number[0]}")
#removing an item from a list
motorcycle.remove("Suzuki")
print(motorcycle)
