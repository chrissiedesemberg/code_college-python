cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
if car == 'bmw':
    print(f"\nYour car is a BMW!")

car = "Audi"
if car.lower() == "audi":
    print("Your car is an Audi")
else:
    print("Your car is not an Audi")