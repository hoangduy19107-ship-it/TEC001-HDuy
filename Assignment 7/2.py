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

car = Car("ABC-123", 142)
print("Duy's car:")
print(f"Registration: {car.reg_num}, Max speed: {car.max_speed} km/h, Current speed: {car.current_speed} km/h, Travelled: {car.travelled_distance} km")

print("\nSpeed changes:")
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed after speeding: {car.current_speed}")
car.accelerate(-200)
print(f"Final speed after emergency brake: {car.current_speed}")
