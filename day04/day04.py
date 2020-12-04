import re

print("advent of code 2020 - day 4")


def process_line(passport, line):
    key_values = line.split(" ")
    for element in key_values:
        (key, value) = element.split(":")
        passport[key] = value


def mandatory_fields_present(passport):
    result = "byr" in passport.keys() and "iyr" in passport.keys() and \
             "eyr" in passport.keys() and "hgt" in passport.keys() and \
             "hcl" in passport.keys() and "ecl" in passport.keys() and \
             "pid" in passport.keys()

    return result


def byr_valid(passport):
    if "byr" not in passport.keys():
        return False

    return 1920 <= int(passport["byr"]) <= 2002


def iyr_valid(passport):
    if "iyr" not in passport.keys():
        return False

    return 2010 <= int(passport["iyr"]) <= 2020


def eyr_valid(passport):
    if "eyr" not in passport.keys():
        return False

    return 2020 <= int(passport["eyr"]) <= 2030


def hgt_valid(passport):
    if "hgt" not in passport.keys():
        return False

    if "cm" in passport["hgt"]:
        return 150 <= int(passport['hgt'][:-2]) <= 193
    elif "in" in passport["hgt"]:
        return 59 <= int(passport['hgt'][:-2]) <= 76
    else:
        return False


def hcl_valid(passport):
    if "hcl" not in passport.keys():
        return False

    # print(f"hair color {passport['hcl']} matches: {re.match('^#[0-9a-f]{6}$', passport['hcl']) is not None}")
    return re.match("^#[0-9a-f]{6}$", passport["hcl"]) is not None


def ecl_valid(passport):
    if "ecl" not in passport.keys():
        return False

    allowed_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return passport["ecl"] in allowed_ecl


def pid_valid(passport):
    if "pid" not in passport.keys():
        return False

    # print(f"pid = {passport['pid']} matches {re.match('^[0-9]{9}$', passport['pid']) is not None}")
    return re.match("^[0-9]{9}$", passport["pid"]) is not None


def reset_passport(passport):
    passport.clear()


# part 1

passport = dict()
valid_passport_counter = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line != "":
            # still in the context of one passport
            process_line(passport, line)
        else:
            # a passport is complete
            if mandatory_fields_present(passport):
                valid_passport_counter += 1
            reset_passport(passport)

# result = 237
print(f"part 1: {valid_passport_counter} passports are valid")

# part 2

passport = dict()
valid_passport_counter = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line != "":
            # still in the context of one passport
            process_line(passport, line)
        else:
            # a passport is complete
            if mandatory_fields_present(passport) and byr_valid(passport) and \
                    iyr_valid(passport) and eyr_valid(passport) and hgt_valid(passport) and \
                    hcl_valid(passport) and ecl_valid(passport) and pid_valid(passport):
                valid_passport_counter += 1
            reset_passport(passport)

# result = 172
print(f"part 2: {valid_passport_counter} passports are valid")
