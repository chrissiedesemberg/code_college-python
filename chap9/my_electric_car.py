from chap9.electric_car import Car

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(120)
print(my_tesla.odometer_reading)
my_tesla.increment_odometer(100)
print(my_tesla.odometer_reading)