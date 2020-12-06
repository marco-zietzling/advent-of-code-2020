print("advent of code 2020 - day 6")

group_answers = []
group_answers1_counter = 0
group_answers2_counter = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()

        if line != "":
            # in the context of one group
            group_answers.append(set(line))

        else:
            # a group is complete
            group_answers1_counter += len(set.union(*group_answers))
            group_answers2_counter += len(set.intersection(*group_answers))
            group_answers.clear()

    # do an extra wrap-up for the last group at the end of the file
    group_answers1_counter += len(set.union(*group_answers))
    group_answers2_counter += len(set.intersection(*group_answers))

# result = 6633
print(f"part 1: sum of count of any yes questions: {group_answers1_counter}")

# result = 3202
print(f"part 2: sum of count of all-yes questions: {group_answers2_counter}")
