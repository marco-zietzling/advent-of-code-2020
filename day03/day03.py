print("advent of code 2020 - day 3")

rows = list()

with open("input.txt") as file:
    for line in file:
        rows.append(line.strip())

line_length = len(rows[0])


def count_trees_on_slope(x_increment, y_increment):
    x = 0
    tree_counter = 0

    for y in range(0, len(rows), y_increment):
        if rows[y][x] == '#':
            tree_counter += 1

        x = (x + x_increment) % line_length

    return tree_counter


# result = 216
print(f"part 1: {count_trees_on_slope(3, 1)} trees encountered")

slope_1_counter = count_trees_on_slope(1, 1)
slope_2_counter = count_trees_on_slope(3, 1)
slope_3_counter = count_trees_on_slope(5, 1)
slope_4_counter = count_trees_on_slope(7, 1)
slope_5_counter = count_trees_on_slope(1, 2)

# result = 6708199680
print(f"part 2: result={slope_1_counter * slope_2_counter * slope_3_counter * slope_4_counter * slope_5_counter}")
