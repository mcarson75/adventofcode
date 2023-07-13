import re

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

fields = {
    "byr": r"^(19[2-9]\d|200[0-2])$",
    "iyr": r"^(201[0-9]|2020)$",
    "eyr": r"^(202[0-9]|2030)$",
    "hgt": r"^(59in|6[0-9]in|7[0-6]in|1[5-8][0-9]cm|19[0-3]cm)$",
    "hcl": r"^#[0-9a-f]{6}$",
    "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
    "pid": r"^[0-9]{9}$",
}

passports = []
passport = {}
for line in lines:
    if line:
        datas = line.split(" ")
        for data in datas:
            field, value = data.split(":")
            passport[field] = value
    else:
        passports.append(passport)
        passport = {}

passports.append(passport)

for passport in passports:
    if all([n in passport.keys() for n in fields.keys()]):
        passport["all_fields"] = True
    else:
        passport["all_fields"] = False
    if passport["all_fields"]:
        passport["valid"] = True
        for f in fields.keys():
            if not re.match(fields[f], passport[f]):
                passport["valid"] = False
                break
    else:
        passport["valid"] = False

part1 = len([p for p in passports if p["all_fields"]])
part2 = len([p for p in passports if p["valid"]])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
