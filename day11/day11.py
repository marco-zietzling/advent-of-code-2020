print("advent of code 2020 - day 11")

num_rows = 0
num_cols = 0


def read_input():
    result = []

    with open("input.txt") as file:
        for line in file:
            result.append(list(line.strip()))

    return result


def check_row(input, row, col):
    result = 0

    if col > 0:
        if input[row][col - 1] == "#":
            result += 1

    if input[row][col] == "#":
        result += 1

    if col < num_cols - 1:
        if input[row][col + 1] == "#":
            result += 1

    return result


def count_occupied_neighbour_seats(input, row, col):
    result = 0

    if row > 0:
        result += check_row(input, row - 1, col)

    result += check_row(input, row, col)

    # if current seat is occupied, remove it from the counter
    if input[row][col] == "#":
        result -= 1

    if row < num_rows - 1:
        result += check_row(input, row + 1, col)

    return result


def execute_iteration(input):
    changes = 0
    result = read_input()

    for row in range(num_rows):
        for col in range(num_cols):
            current_seat = input[row][col]
            surrounding_occupied_seats = count_occupied_neighbour_seats(input, row, col)

            if current_seat == "#" and surrounding_occupied_seats >= 4:
                result[row][col] = "L"
                changes += 1
            elif current_seat == "L" and surrounding_occupied_seats == 0:
                result[row][col] = "#"
                changes += 1
            else:
                result[row][col] = current_seat

    return changes, result


def count_occupied_seats(input):
    result = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if input[row][col] == "#":
                result += 1

    return result


state = read_input()
num_rows = len(state)
num_cols = len(state[0])

iteration_counter = 0

while True:
    changes, state = execute_iteration(state)
    iteration_counter += 1
    if changes == 0:
        break

occupied_seats = count_occupied_seats(state)

print(f"part 1: final state has {occupied_seats} occupied seats after {iteration_counter} iterations")
