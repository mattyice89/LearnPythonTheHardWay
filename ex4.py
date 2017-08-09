cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Expalin the error:
# formula Zed used was:
# average_passengers_per_car = car_pool_capacity / passenger
# error received: name 'car_pool_capacity' is not defined

# error received was because the correct variable name is
# 'carpool_capacity', not 'car_pool_capacity'
