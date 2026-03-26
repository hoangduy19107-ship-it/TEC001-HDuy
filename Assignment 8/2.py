class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        else:
            print(f"Elevator already at top floor {self.top_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        else:
            print(f"Elevator already at bottom floor {self.bottom_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Target floor {target_floor} is out of range")
            return
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator is now at floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 1 <= elevator_number <= len(self.elevators):
            self.elevators[elevator_number - 1].go_to_floor(destination_floor)
        else:
            print(f"Invalid elevator number {elevator_number}")

if __name__ == '__main__':
    building = Building(1, 10, 3)
    building.run_elevator(1, 4)
    building.run_elevator(2, 3)
    building.run_elevator(3, 9)
