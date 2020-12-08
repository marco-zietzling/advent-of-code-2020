import re

print("advent of code 2020 - day 7")


def extract_number_of_bags(_bag: str):
    _matched_numbers = re.findall("[0-9]+", _bag)
    _bag = re.sub("bags", "", _bag)
    _bag = re.sub("bag", "", _bag)
    _bag = re.sub("no other", "", _bag)
    _bag = re.sub("[0-9]+", "", _bag)
    _bag = _bag.strip()

    _number = 0
    if _matched_numbers:
        _number = _matched_numbers[0]

    # print(f"result is ({_number}, {_bag})")
    return _number, _bag


def load_bag_rules():
    _result = dict()

    with open("input.txt") as _file:
        for _line in _file:
            (_container_bag, _contained_bags) = _line.strip().split(" contain ")
            (_, _cr_bag_name) = extract_number_of_bags(_container_bag)

            _contained_bags = _contained_bags.strip(".")
            _contained_bag_entries = _contained_bags.split(", ")
            _clean_contained_bag_entries = []

            for _entry in _contained_bag_entries:
                (_cd_bag_number, _cd_bag_name) = extract_number_of_bags(_entry)
                if _cd_bag_name != "":
                    _clean_contained_bag_entries.append((_cd_bag_number, _cd_bag_name))

            _result[_cr_bag_name] = _clean_contained_bag_entries

    # print(_result)
    return _result


def calculate_part_1():
    _bag_queue = ["shiny gold"]
    _result_bag_set = set()
    _bag_ruleset = load_bag_rules()

    while _bag_queue:
        # print(f"current queue: {_bag_queue}")
        _current_bag = _bag_queue[0]
        _bag_queue.remove(_current_bag)
        # print(f"current bag: {_current_bag}")

        for _rule in _bag_ruleset:
            # print(f"current rule: '{_rule}' ->  {_bag_ruleset[_rule]}")
            if _current_bag in list(map(lambda x: x[1], _bag_ruleset[_rule])):
                if _rule not in _result_bag_set:
                    _bag_queue.append(_rule)
                    _result_bag_set.add(_rule)

    print(f"{_result_bag_set}")
    return len(_result_bag_set)


def calculate_part_2(_bag_ruleset, _bag="shiny gold"):
    _result = 1
    _contained_bags = _bag_ruleset[_bag]
    # print(f"current contained bags: {_contained_bags}")

    for (_amount, _contained_bag) in _contained_bags:
        # print(f"amount={_amount} of bags={_contained_bag}")
        _result += int(_amount) * calculate_part_2(_bag_ruleset, _contained_bag)

    return _result


# result = 335
print(f"part 1: {calculate_part_1()} bags can contain directly or indirectly the shiny gold bag")

bag_ruleset = load_bag_rules()

# result = 2431 (in order to cater for the shiny gold bag itself, we need to substract -1 from the final result
print(f"part 2: {calculate_part_2(bag_ruleset) - 1} other bags are contained within a shiny gold bag")
