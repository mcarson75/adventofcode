import re

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


class group:
    line_regex = r"(\d+) units each with (\d+) hit points (\([a-zA-Z ,;]+\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)"
    weakness_regex = r"weak to ([a-zA-Z, ]+)"
    immune_regex = r"immune to ([a-zA-Z, ]+)"

    def __init__(self, line, g, boost):
        self.num = g
        match = re.search(self.line_regex, line)
        self.attacker = None
        self.target = None
        size, hit, mod, damage, self.damage_type, initiative = match.groups()
        self.size, self.hit, self.damage, self.initiative = (
            int(size),
            int(hit),
            int(damage) + boost,
            int(initiative),
        )
        self.weakness = []
        self.immune = []
        if mod:
            weakness = re.search(self.weakness_regex, mod)
            immune = re.search(self.immune_regex, mod)

            if weakness:
                self.weakness = weakness.group(1).split(", ")

            if immune:
                self.immune = immune.group(1).split(", ")

    def __repr__(self):
        return str(self.num)

    @property
    def effective_power(self):
        return self.size * self.damage

    def mod(self, damage_type):
        if damage_type in self.immune:
            return 0
        elif damage_type in self.weakness:
            return 2
        return 1

    def target_sort(self, damage_type):
        return (self.mod(damage_type), self.effective_power, self.initiative)

    def choose_target(self, others):
        self.target = None
        if self.effective_power > 0:
            targets = sorted(
                [o for o in others if not o.attacker and o.size > 0],
                key=lambda o: o.target_sort(self.damage_type),
                reverse=True,
            )
            if targets:
                self.target = targets[0]
                self.target.attacker = self

    def attacked(self, damage, type):
        self.attacker = None
        if type in self.immune:
            return
        if type in self.weakness:
            damage *= 2

        self.size -= damage // self.hit

        if self.size < 0:
            self.size = 0

    def attack(self):
        if self.target:
            self.target.attacked(self.effective_power, self.damage_type)


def total_size(army):
    return sum(g.size for g in army)


def play_game(boost=0):
    immune = set()
    infection = set()
    current = None
    num = 1
    for line in lines:
        if "Immune" in line:
            current = "immune"
            continue
        elif "Infection" in line:
            current = "infection"
            num = 1
            continue

        if line and current == "immune":
            immune.add(group(line, num, boost))
        elif line and current == "infection":
            infection.add(group(line, num, 0))

        num += 1

    last_battle = total_size(immune) + total_size(infection)
    n = 1
    while total_size(immune) > 0 and total_size(infection) > 0:
        if n == 143:
            print("stop")
        for i in sorted(
            list(immune), key=lambda g: (g.effective_power, g.initiative), reverse=True
        ):
            i.choose_target(infection)
        for i in sorted(
            list(infection),
            key=lambda g: (g.effective_power, g.initiative),
            reverse=True,
        ):
            i.choose_target(immune)

        for i in sorted(
            list(immune | infection), key=lambda g: g.initiative, reverse=True
        ):
            i.attack()

        immune = set(i for i in immune if i.effective_power > 0)
        infection = set(i for i in infection if i.effective_power > 0)

        with open("output2.txt", "a") as f:
            f.write(f"Iteration: {n}\n")
            f.write(f"Immune: {[g.size for g in immune]}\n")
            f.write(f"Infection: {[g.size for g in infection]}\n")
            f.write(f"\n")

        if total_size(immune) + total_size(infection) != last_battle:
            last_battle = total_size(immune) + total_size(infection)
        else:
            return "tie", 0
        n += 1

    if total_size(immune) == 0:
        return "infection", total_size(infection)
    else:
        return "immune", total_size(immune)


play_game(boost=16)
_, part1 = play_game()

print(f"Part 1: {part1}")

boost = 1
while True:
    winner, score = play_game(boost=boost)
    print(f"Boost: {boost}, Winner: {winner}, Score: {score}")
    if winner == "immune":
        break
    boost += 1

print(f"Part 2: {score}")
