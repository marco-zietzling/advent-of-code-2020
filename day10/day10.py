print("advent of code 2020 - day 10")


def read_joltages():
    result = []

    with open("input.txt") as file:
        for line in file:
            result.append(int(line.strip()))

    return result


joltages = read_joltages()
joltages.append(0)
joltages.append(max(joltages) + 3)
joltages.sort()

one_jolt_differences = 0
three_jolt_differences = 0

last_joltage = 0  # start from the seat outlet

for current_joltage in joltages:
    if current_joltage - last_joltage == 1:
        one_jolt_differences += 1
    elif current_joltage - last_joltage == 3:
        three_jolt_differences += 1

    last_joltage = current_joltage

# result = 2484
print(f"part 1: result = {one_jolt_differences * three_jolt_differences}")

joltages = read_joltages()
joltages.append(0)
joltages.append(max(joltages) + 3)
joltages.sort()


def count_possibilities(current_index=0):
    current_joltage = joltages[current_index]
    result = 0

    if current_index == len(joltages) - 1:
        return 1

    for i in range(1, 4):
        if current_index + i < len(joltages):
            next_joltage = joltages[current_index + i]
            if next_joltage - current_joltage <= 3:
                result += count_possibilities(current_index + i)

    return result


# does not work... very long runtime
print(f"part 2: result = {count_possibilities()}")
