print("advent of code 2020 - day 12")

directions = ["N", "E", "S", "W"]
current_ship_dir_index = 1
current_ship_pos_x1 = 0
current_ship_pos_y1 = 0
current_ship_pos_x2 = 0
current_ship_pos_y2 = 0
current_waypoint_pos_x = 10
current_waypoint_pos_y = 1

instructions = []

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        instructions.append((line[:1], int(line[1:])))


def rotate_waypoint(rotation):
    global current_waypoint_pos_x
    global current_waypoint_pos_y

    old_x = current_waypoint_pos_x
    old_y = current_waypoint_pos_y

    if rotation == -1 or rotation == 3:
        current_waypoint_pos_x = - old_y
        current_waypoint_pos_y = old_x
    elif rotation == -2 or rotation == 2:
        current_waypoint_pos_x = - old_x
        current_waypoint_pos_y = - old_y
    elif rotation == -3 or rotation == 1:
        current_waypoint_pos_x = old_y
        current_waypoint_pos_y = - old_x
    else:
        print(f"unknown rotation encountered: {rotation}")


for action, value in instructions:
    if action == "N":
        current_ship_pos_y1 += value
        current_waypoint_pos_y += value
    elif action == "S":
        current_ship_pos_y1 -= value
        current_waypoint_pos_y -= value
    elif action == "E":
        current_ship_pos_x1 += value
        current_waypoint_pos_x += value
    elif action == "W":
        current_ship_pos_x1 -= value
        current_waypoint_pos_x -= value
    elif action == "L":
        current_ship_dir_index = (current_ship_dir_index - (value // 90)) % 4
        rotate_waypoint(- (value // 90))
    elif action == "R":
        current_ship_dir_index = (current_ship_dir_index + (value // 90)) % 4
        rotate_waypoint((value // 90))
    elif action == "F":
        if directions[current_ship_dir_index] == "N":
            current_ship_pos_y1 += value
        elif directions[current_ship_dir_index] == "S":
            current_ship_pos_y1 -= value
        elif directions[current_ship_dir_index] == "E":
            current_ship_pos_x1 += value
        elif directions[current_ship_dir_index] == "W":
            current_ship_pos_x1 -= value

        current_ship_pos_x2 += value * current_waypoint_pos_x
        current_ship_pos_y2 += value * current_waypoint_pos_y
    else:
        print(f"invalid action: {action}")

# result = 1441
print(f"part 1: distance to origin = {abs(current_ship_pos_x1) + abs(current_ship_pos_y1)}")

# result = 61616
print(f"part 2: distance to origin = {abs(current_ship_pos_x2) + abs(current_ship_pos_y2)}")
