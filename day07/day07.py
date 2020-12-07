import re

print("advent of code 2020 - day 7")


def extract_number_of_bags(bag: str):
    matched_numbers = re.findall("[0-9]+", bag)
    bag = re.sub("bags", "", bag)
    bag = re.sub("bag", "", bag)
    bag = re.sub("no other", "", bag)
    bag = re.sub("[0-9]+", "", bag)
    bag = bag.strip()

    number = 0
    if matched_numbers:
        number = matched_numbers[0]

    # print(f"result is ({number}, {bag})")
    return number, bag


def load_bag_rules():
    result = dict()

    with open("input.txt") as file:
        for line in file:
            (container_bag, contained_bags) = line.strip().split(" contain ")
            (_, cr_bag_name) = extract_number_of_bags(container_bag)

            contained_bags = contained_bags.strip(".")
            contained_bag_entries = contained_bags.split(", ")
            clean_contained_bag_entries = []

            for entry in contained_bag_entries:
                (cd_bag_number, cd_bag_name) = extract_number_of_bags(entry)
                if cd_bag_name != "":
                    clean_contained_bag_entries.append((cd_bag_number, cd_bag_name))

            result[cr_bag_name] = clean_contained_bag_entries

    # print(result)
    return result


def calculate_part_1():
    bag_queue = ["shiny gold"]
    result_bag_set = set()
    bag_ruleset = load_bag_rules()

    while bag_queue:
        # print(f"current queue: {bag_queue}")
        current_bag = bag_queue[0]
        bag_queue.remove(current_bag)
        # print(f"current bag: {current_bag}")

        for rule in bag_ruleset:
            # print(f"current rule: '{rule}' ->  {bag_ruleset[rule]}")
            if current_bag in list(map(lambda x: x[1], bag_ruleset[rule])):
                if rule not in result_bag_set:
                    bag_queue.append(rule)
                    result_bag_set.add(rule)

    print(f"{result_bag_set}")
    return len(result_bag_set)


# result = 335
print(f"part 1: {calculate_part_1()} bags can contain directly or indirectly the shiny gold bag")
