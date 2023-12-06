import re

inp_imm = """123 units each with 8524 hit points with an attack that does 612 slashing damage at initiative 11
148 units each with 4377 hit points (weak to slashing, bludgeoning) with an attack that does 263 cold damage at initiative 1
6488 units each with 2522 hit points (weak to fire) with an attack that does 3 bludgeoning damage at initiative 19
821 units each with 8034 hit points (immune to cold, bludgeoning) with an attack that does 92 cold damage at initiative 17
1163 units each with 4739 hit points (weak to cold) with an attack that does 40 bludgeoning damage at initiative 14
1141 units each with 4570 hit points (weak to fire, slashing) with an attack that does 32 radiation damage at initiative 18
108 units each with 2954 hit points with an attack that does 262 radiation damage at initiative 8
4752 units each with 6337 hit points (weak to bludgeoning, cold; immune to slashing) with an attack that does 13 cold damage at initiative 20
4489 units each with 9894 hit points (weak to slashing) with an attack that does 20 slashing damage at initiative 12
331 units each with 12535 hit points with an attack that does 300 slashing damage at initiative 15"""

inp_infection = """853 units each with 13840 hit points (weak to bludgeoning, cold) with an attack that does 26 fire damage at initiative 3
450 units each with 62973 hit points (weak to slashing) with an attack that does 220 fire damage at initiative 13
3777 units each with 35038 hit points (weak to cold) with an attack that does 18 radiation damage at initiative 7
96 units each with 43975 hit points (immune to bludgeoning; weak to cold, slashing) with an attack that does 862 radiation damage at initiative 16
1536 units each with 14280 hit points (weak to cold, fire; immune to bludgeoning) with an attack that does 18 slashing damage at initiative 2
3696 units each with 36133 hit points (weak to radiation; immune to cold, fire) with an attack that does 18 bludgeoning damage at initiative 10
3126 units each with 39578 hit points (weak to cold) with an attack that does 22 radiation damage at initiative 4
1128 units each with 13298 hit points (weak to bludgeoning, slashing) with an attack that does 23 fire damage at initiative 6
7539 units each with 6367 hit points (weak to fire; immune to radiation) with an attack that does 1 slashing damage at initiative 5
1886 units each with 45342 hit points (weak to fire, cold) with an attack that does 45 cold damage at initiative 9"""


class group:
    def __init__(
        self, n, hp_each, weaknesses, immunities, atk_dmg, atk_type, initiative, team
    ):
        self.n = n
        self.hp_each = hp_each
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.atk_dmg = atk_dmg
        self.atk_type = atk_type
        self.initiative = initiative
        self.team = team

    def __repr__(self):
        return "group({!r})".format(self.__dict__)

    @property
    def eff_power(self):
        return self.n * self.atk_dmg

    def dmg_to(self, other):
        return self.eff_power * (
            0
            if self.atk_type in other.immunities
            else 2
            if self.atk_type in other.weaknesses
            else 1
        )


def parse(st, team, boost=0):
    res = []
    for i in st.split("\n"):
        g = re.match(
            r"(\d+) units each with (\d+) hit points (?:\((.*?)\) )?with an attack that does (\d+) (\S+) damage at initiative (\d+)",
            i,
        )
        n = int(g.group(1))
        hp = int(g.group(2))
        weaknesses = set()
        immunities = set()
        wi = g.group(3)
        if wi is not None:
            for cmp in wi.split("; "):
                if cmp.startswith("immune to "):
                    immunities |= set(cmp[len("immune to ") :].split(", "))
                elif cmp.startswith("weak to "):
                    weaknesses |= set(cmp[len("weak to ") :].split(", "))
        dmg = int(g.group(4))
        typ = g.group(5)
        initiative = int(g.group(6))
        res.append(
            group(n, hp, weaknesses, immunities, dmg + boost, typ, initiative, team)
        )
    return res


def get_team(s):
    if s is None:
        return "stalemate"
    for i in s:
        return i.team


def run_combat(imm_inp, inf_inp, boost=0):
    immune_system = set(parse(imm_inp, "immune", boost))
    infection = set(parse(inf_inp, "infection"))
    n = 1
    while immune_system and infection:
        potential_combatants = immune_system | infection
        attacking = {}
        for combatant in sorted(
            immune_system | infection,
            key=lambda x: (x.eff_power, x.initiative),
            reverse=True,
        ):
            try:
                s = max(
                    (
                        x
                        for x in potential_combatants
                        if x.team != combatant.team and combatant.dmg_to(x) != 0
                    ),
                    key=lambda x: (combatant.dmg_to(x), x.eff_power, x.initiative),
                )
            except ValueError as e:
                attacking[combatant] = None
                continue
            potential_combatants.remove(s)
            attacking[combatant] = s
        did_damage = False
        for combatant in sorted(
            immune_system | infection, key=lambda x: x.initiative, reverse=True
        ):
            if combatant.n <= 0:
                continue
            atk = attacking[combatant]
            if atk is None:
                continue
            dmg = combatant.dmg_to(atk)
            n_dead = dmg // atk.hp_each
            if n_dead > 0:
                did_damage = True
            atk.n -= n_dead
            if atk.n <= 0:
                immune_system -= {atk}
                infection -= {atk}

        if not did_damage:
            return None
        # print("NEW ROUND")
        # print("immune_system", immune_system)
        # print("infection", infection)
        with open("output.txt", "a") as f:
            f.write(f"Iteration: {n}\n")
            f.write(f"Immune: {[g.n for g in immune_system]}\n")
            f.write(f"Infection: {[g.n for g in infection]}\n")
            f.write(f"\n")
        n += 1
    print(f"Boost: {boost}")
    print(f"Immune: {sum([g.n for g in immune_system])}")
    print(f"Infection: {sum([g.n for g in infection])}")
    winner = max(immune_system, infection, key=len)
    return winner


winner = run_combat(inp_imm, inp_infection)
print("Part 1:", sum(x.n for x in winner))

boost_min = 0
boost_max = 1
while get_team(run_combat(inp_imm, inp_infection, boost_max)) != "immune":
    boost_max *= 2
    # print(boost_max)

import math

while boost_min != boost_max:
    pow = (boost_min + boost_max) // 2
    cr = run_combat(inp_imm, inp_infection, pow)
    res = get_team(cr)
    if res != "immune":
        boost_min = math.ceil((boost_min + boost_max) / 2)
    else:
        boost_max = pow
    # print(boost_min, boost_max)
print("Boost:", boost_max)
print("Part 2:", sum(x.n for x in run_combat(inp_imm, inp_infection, boost_max)))
