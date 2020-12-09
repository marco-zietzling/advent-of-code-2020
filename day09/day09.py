print("advent of code 2020 - day 9")


def read_numbers():
    result = []

    with open("input.txt") as file:
        for line in file:
            result.append(int(line.strip()))

    # print(f"{result}")
    return result


def check_for_valid_sum(numbers: list[int], current_index: int):
    target_number = numbers[current_index]

    for i in range(current_index - 25, current_index):
        for j in range(i + 1, current_index):
            # print(f"checking at indices {i} and {j} with values {numbers[i]} and {numbers[j]}")
            if numbers[i] + numbers[j] == target_number:
                return True

    return False


numbers = read_numbers()
current_index = 25

while check_for_valid_sum(numbers, current_index):
    current_index += 1

target_index = current_index
target_number = numbers[current_index]

# result = 2089807806
print(f"part 1: number that does not is sum of previous 25 numbers = {target_number} at index {target_index}")

for i in range(target_index):
    current_sum = numbers[i]

    for j in range(i + 1, target_index):
        current_sum += numbers[j]

        if current_sum == target_number:
            min_index = i
            max_index = j
            # print(f"found it with min index = {min_index} and max index = {max_index}")
        elif current_sum > target_number:
            break

minimum = 9999999999
maximum = 0
for i in range(min_index, max_index + 1):
    if numbers[i] < minimum:
        minimum = numbers[i]
    elif numbers[i] > maximum:
        maximum = numbers[i]

# result = 245848639
print(f"part 2: sum of smallest number {minimum} and largest number {maximum} = {minimum + maximum}")
