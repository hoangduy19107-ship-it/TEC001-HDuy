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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration':<12} {'Max Speed':<10} {'Current Speed':<14} {'Travelled Distance':<18}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.reg_num:<12} {car.max_speed:<10} {car.current_speed:<14} {car.travelled_distance:<18.1f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

if __name__ == '__main__':
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(150, 200)
        cars.append(Car(f"ABC-{i}", max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hour = 0
    while not race.race_finished():
        race.hour_passes()
        hour += 1
        if hour % 10 == 0:
            print(f"\nHour {hour}:")
            race.print_status()

    print(f"\nRace finished after {hour} hours!")
    race.print_status()
