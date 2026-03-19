import random

class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed after accelerations: {car.current_speed} km/h")
car.accelerate(-200)
print(f"Final speed after emergency brake: {car.current_speed} km/h")

car.travelled_distance = 2000
car.current_speed = 60
car.drive(1.5)
print(f"Registration: {car.reg_num}, Max speed: {car.max_speed} km/h, Current speed: {car.current_speed} km/h, Travelled: {car.travelled_distance} km")

print("\nPart 4: Car Race")
cars = []
for i in range(1, 11):
    max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i}", max_speed))

hour = 0
while True:
    hour += 1
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
    if any(car.travelled_distance >= 10000 for car in cars):
        break

print(f"{'Registration':<12} {'Max Speed':<10} {'Current Speed':<14} {'Travelled Distance':<18}")
print("-" * 60)
for car in cars:
    print(f"{car.reg_num:<12} {car.max_speed:<10} {car.current_speed:<14} {car.travelled_distance:<18.1f}")
