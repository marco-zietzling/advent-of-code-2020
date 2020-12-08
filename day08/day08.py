print("advent of code 2020 - day 8")


def read_program():
    _instructions = []

    with open("input.txt") as file:
        for line in file:
            (_operation, _argument) = line.strip().split(" ")
            _instructions.append((_operation, int(_argument)))

    return _instructions


def run_program_until_infloop(_instructions: list[(str, int)]):
    _accumulator = 0
    _index = 0
    _indices_visited = set()
    _infinite_loop_encountered = False

    while True:
        _indices_visited.add(_index)
        (_operation, _argument) = _instructions[_index]
        # print(f"current instruction: {_operation} {_argument}")

        if _operation == "nop":
            _index += 1
        elif _operation == "acc":
            _accumulator += _argument
            _index += 1
        elif _operation == "jmp":
            _index += _argument
        else:
            raise Exception(f"unknown _operation encountered: {_operation}")

        if _index in _indices_visited:
            _infinite_loop_encountered = True
            break
        elif _index >= len(_instructions):
            break

    return _infinite_loop_encountered, _accumulator


instructions = read_program()
infinite_loop, accumulator = run_program_until_infloop(instructions)

# result = 2034
print(f"part 1: value of accumulator before infinite loop = {accumulator}")

current_index_to_modify = 0
while True:

    instructions = read_program()
    (operation, argument) = instructions[current_index_to_modify]

    if operation == "nop":
        instructions[current_index_to_modify] = ("jmp", argument)
    elif operation == "jmp":
        instructions[current_index_to_modify] = ("nop", argument)

    infinite_loop, accumulator = run_program_until_infloop(instructions)
    current_index_to_modify += 1

    if not infinite_loop:
        break

# result = 672
print(f"part 2: value of accumulator without infinite loop = {accumulator}")
