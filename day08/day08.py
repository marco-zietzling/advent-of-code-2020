print("advent of code 2020 - day 8")


def read_program():
    instructions = []

    with open("input.txt") as file:
        for line in file:
            (operation, argument) = line.strip().split(" ")
            instructions.append((operation, int(argument)))

    return instructions


def run_program_until_inflp(instructions: list[(str, int)]):
    accumulator = 0
    index = 0
    indices_visited = set()
    infinite_loop_encountered = False

    while True:
        indices_visited.add(index)
        (operation, argument) = instructions[index]
        # print(f"current instruction: {operation} {argument}")

        if operation == "nop":
            index += 1
        elif operation == "acc":
            accumulator += argument
            # print(f"current value of accumulator = {accumulator}")
            index += 1
        elif operation == "jmp":
            index += argument
        else:
            raise Exception(f"unknown operation encountered: {operation}")

        if index in indices_visited:
            infinite_loop_encountered = True
            break
        elif index >= len(instructions):
            break

    return infinite_loop_encountered, accumulator


instructions = read_program()
infinite_loop, accumulator = run_program_until_inflp(instructions)

# result = 2034
print(f"part 1: value of accumulator before infinite loop = {accumulator}")
