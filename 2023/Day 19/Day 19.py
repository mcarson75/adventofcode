import re
from math import prod

rule_input, parts = [
    g.splitlines()
    for g in open("input.txt", "r", encoding="utf-8").read().strip().split("\n\n")
]


def evaluate_rule(name, x, m, a, s):
    while name not in "AR":
        for _rule in workflows[name][:-1]:
            rule, next_rule = _rule.split(":")
            if eval(rule):
                name = next_rule
                break
        else:
            name = workflows[name][-1]
    return x + m + a + s if name == "A" else 0


def find_rules(current, conditions):
    if current == "A":
        rules.append(conditions)
    elif current != "R":
        for rule in workflows[current][:-1]:
            condition, next_workflow = rule.split(":")
            find_rules(next_workflow, conditions + [condition])
            if condition[1] == "<":
                conditions.append(condition.replace("<", ">="))
            elif condition[1] == ">":
                conditions.append(condition.replace(">", "<="))
        else:
            next_workflow = workflows[current][-1]
            find_rules(next_workflow, conditions)


def rules_match(conditions):
    maxs = {x: 4001 for x in "xmas"}
    mins = {x: 0 for x in "xmas"}
    for cond in conditions:
        type, cond, num = re.match(r"([xmas])(<=|>=|<|>)(\d+)", cond).groups()
        if cond == "<":
            maxs[type] = min(maxs[type], int(num))
        elif cond == "<=":
            maxs[type] = min(maxs[type], int(num) + 1)
        if cond == ">":
            mins[type] = max(mins[type], int(num))
        if cond == ">=":
            mins[type] = max(mins[type], int(num) - 1)

    return prod([maxs[k] - mins[k] - 1 for k in maxs])


workflows = {
    name: rules[:-1].split(",")
    for name, rules in (line.split("{") for line in rule_input)
}
rules = []
find_rules("in", [])

part1 = sum(
    [evaluate_rule("in", *list(map(int, re.findall(r"\d+", part)))) for part in parts]
)
part2 = sum([rules_match(r) for r in rules])


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
