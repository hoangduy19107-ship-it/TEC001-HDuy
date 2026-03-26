class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        print(f"Elevator started at floor {self.current_floor} (bottom={self.bottom_floor}, top={self.top_floor})")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Floor up: now at {self.current_floor}")
        else:
            print(f"Already at top floor {self.top_floor}; cannot go up")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Floor down: now at {self.current_floor}")
        else:
            print(f"Already at bottom floor {self.bottom_floor}; cannot go down")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            raise ValueError(f"Target floor {target_floor} out of range [{self.bottom_floor}, {self.top_floor}]")

        if self.current_floor == target_floor:
            print(f"Already at floor {self.current_floor}; no movement needed")
            return

        print(f"Going to floor {target_floor} from {self.current_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")

if __name__ == '__main__':
    h = Elevator(1, 10)

    h.go_to_floor(3)
    h.go_to_floor(h.bottom_floor)
