class person:
    def __init__( self , _name , _age):
        self.name = _name
        self.age = _age
    
    def sayHi(self):   
        print("hello,my name is " +str(self.name) +" and i am " +str(self.age))
person1 = person('moses', 18)        
person1.sayHi()
person2 = person('ngaruiya', 19)
person2.sayHi()