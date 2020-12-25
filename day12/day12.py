print("advent of code 2020 - day 12")

directions = ["N", "E", "S", "W"]
current_dir_index = 1
current_pos_x = 0
current_pos_y = 0

instructions = []

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        instructions.append((line[:1], int(line[1:])))

for action, value in instructions:
    if action == "N":
        current_pos_y += value
    elif action == "S":
        current_pos_y -= value
    elif action == "E":
        current_pos_x += value
    elif action == "W":
        current_pos_x -= value
    elif action == "L":
        current_dir_index = (current_dir_index - (value // 90)) % 4
    elif action == "R":
        current_dir_index = (current_dir_index + (value // 90)) % 4
    elif action == "F":
        if directions[current_dir_index] == "N":
            current_pos_y += value
        elif directions[current_dir_index] == "S":
            current_pos_y -= value
        elif directions[current_dir_index] == "E":
            current_pos_x += value
        elif directions[current_dir_index] == "W":
            current_pos_x -= value
    else:
        print(f"invalid action: {action}")

# result = 1441
print(f"part 1: distance to origin = {abs(current_pos_x) + abs(current_pos_y)}")
