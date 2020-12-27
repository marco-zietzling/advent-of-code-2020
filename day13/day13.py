from dataclasses import dataclass

print("advent of code 2020 - day 13")


@dataclass
class Bus:
    id: int
    next_departure: int


with open("input.txt") as file:
    lines = file.readlines()

earliest_timestamp = int(lines[0].strip())
bus_ids = lines[1].strip().split(",")

busses = []

for bus_id in bus_ids:
    if bus_id != "x":
        busses.append(Bus(id=int(bus_id), next_departure=0))

for bus in busses:
    while True:
        bus.next_departure += bus.id
        if bus.next_departure >= earliest_timestamp:
            break

busses.sort(key=lambda i: i.next_departure)
bus_id = busses[0].id
bus_diff = busses[0].next_departure - earliest_timestamp

# result = 4315
print(f"part 1: Bus ID {bus_id} wait for {bus_diff} minutes = {bus_id * bus_diff}")
