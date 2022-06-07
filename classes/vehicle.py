class vehicle :
    def __init__(car, _mileage, _speed):
        car.mileage = _mileage
        car.speed = _speed
    def sayHi(car):
        print("vehicle maximum speed : " + str(car.speed) + "car mileage : " + str(car.mileage))
car1 = vehicle(257,3000)
car1.sayHi()
       