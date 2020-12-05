print("advent of code 2020 - day 5")


def extract_row(passport):
    row_code = passport[0:7]
    row_code = row_code.replace("B", "1")
    row_code = row_code.replace("F", "0")
    return int(row_code, 2)


def extract_col(passport):
    col_code = passport[7:10]
    col_code = col_code.replace("R", "1")
    col_code = col_code.replace("L", "0")
    return int(col_code, 2)


def calculate_seat_id(row, column):
    return row * 8 + column


highest_seat_id = 0
seat_ids = []

with open("input.txt") as file:
    for line in file:
        passport = line.strip()
        row = extract_row(passport)
        col = extract_col(passport)
        seat_id = calculate_seat_id(row, col)
        seat_ids.append(seat_id)

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

# result = 892
print(f"part 1: highest seat ID = {highest_seat_id}")

seat_ids.sort()

# result = 625
for i in range(len(seat_ids) - 1):
    if seat_ids[i + 1] - seat_ids[i] > 1:
        print(f"{seat_ids[i]} < my seat Id < {seat_ids[i + 1]}")
        print(f"part 2: my seat ID = {seat_ids[i] + 1}")
