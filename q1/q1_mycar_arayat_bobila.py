# da car game
class Car:
    def __init__(self,brand,model,battery=33):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self, distance):
        s = distance / 25
        self.battery = self.battery - s
        print(f"You traveled {distance} km")
        print(f"Your {self.brand} {self.model} has {self.battery} wH left")
    def charge(self, wH):
        self.battery = self.battery + wH
        print(f"you charged {wH} wH")
        print(f"Your {self.brand} {self.model} has {self.battery} wH left")

brand = input("What is the brand of your car?: ").upper()
model = input("What is the model of your car?: ").upper()
myCar = Car(brand,model)
while myCar.battery > 0:
    command = input("What do you want to do? (GO, CHARGE): ").upper()
    if command == "GO":
        distance = int(input("How far?: "))
        myCar.go(distance)
    elif command == "CHARGE":
        wH = int(input("How much?: "))
        myCar.charge(wH)
    else:
        print("Invalid command!")
print("Your car ran out of battery!")
