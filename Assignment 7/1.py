class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)
print("Duy's car:")
print(f"Registration: {car.reg_num}, Max speed: {car.max_speed} km/h, Current speed: {car.current_speed} km/h, Travelled: {car.travelled_distance} km")
