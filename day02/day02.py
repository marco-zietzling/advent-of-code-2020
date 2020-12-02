print("advent of code 2020 - day 2")


# part 1
def is_valid_password_part1(password_with_policy):
    (policy, letter, password) = password_with_policy.split(" ")
    (min_occurrences, max_occurrences) = map(int, policy.split("-"))
    letter = letter[0]
    # print(f"min:{min_occurrences} max:{max_occurrences} letter:{letter} password:{password}")
    return min_occurrences <= password.count(letter) <= max_occurrences


# part 2
def is_valid_password_part2(password_with_policy):
    (policy, letter, password) = password_with_policy.split(" ")
    (first_position, second_position) = map(int, policy.split("-"))
    letter = letter[0]
    # print(f"first_pos:{first_position} second_pos:{second_position} letter:{letter} password:{password}")
    first_match = password[first_position - 1] == letter
    second_match = password[second_position - 1] == letter
    return (first_match and not second_match) or (not first_match and second_match)


part1_counter = 0
part2_counter = 0

with open("input.txt") as file:
    for line in file:
        if is_valid_password_part1(line):
            part1_counter += 1
        if is_valid_password_part2(line):
            part2_counter += 1

# result = 550
print(f"part 1: result={part1_counter}")

print(f"part 2: result={part2_counter}")
