print("advent of code 2020 - day 1")

entries = list()

with open("input.txt") as file:
    for line in file:
        entries.append(int(line))

# part 1
for i in range(0, len(entries)):
    for j in range(i + 1, len(entries)):
        if entries[i] + entries[j] == 2020:
            print(f"first entry = {entries[i]}; second entry = {entries[j]}")

            # result = 878724
            print(f"part 1: result = {entries[i] * entries[j]}")

# part 2
for i in range(0, len(entries)):
    for j in range(i + 1, len(entries)):
        for k in range(j + 1, len(entries)):
            if entries[i] + entries[j] + entries[k] == 2020:
                print(f"first entry = {entries[i]}; second entry = {entries[j]}; third entry = {entries[k]}")

                # result = 201251610
                print(f"part 2: result = {entries[i] * entries[j] * entries[k]}")
