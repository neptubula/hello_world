# 定义变量 cars: 汽车数量
cars = 100
# 定义变量 space_in_a_car: 每个车座位数
space_in_a_car = 4
# 定义变量 drivers: 司机数量
drivers = 30
# 定义变量 passengers: 乘客数量
passengers = 90
# 定义变量 cars_not_driven: 不能开动车的数量
cars_not_driven = cars - drivers
# 定义变量 cars_driven: 能开动的车的数量
cars_driven = drivers
# 定义变量 carpool_capacity: 车载客总量
carpool_capacity = cars_driven * space_in_a_car
# 定义变量 average_passengers_per_car: 车载客平均数
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to pull about", average_passengers_per_car, "in each car.")
