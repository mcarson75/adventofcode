from copy import deepcopy

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

class spell:
    def __init__(self, name, cost, turns, damage, armor, heal, mana):
        self.name = name
        self.cost = cost
        self.turns = turns
        self.damage = damage
        self.armor = armor
        self.heal = heal
        self.mana = mana

missile = spell("Missile", 53, 0, 4, 0, 0, 0)   
drain = spell("Drain", 73, 0, 2, 0, 2, 0) 
shield = spell("Shield", 113, 6, 0, 7, 0, 0)
poison = spell("Poison", 173, 6, 3, 0, 0, 0)
recharge = spell("Recharge", 229, 5, 0, 0, 0, 101)

spells = [missile, drain, shield, poison, recharge]

def play(bossHP, playerHP, playerMana, activeSpells, playerTurn, manaUsed, loseHitPoint = False, cheapest = 10000):
    bossDmg = 9
    playerArmor = 0

    if loseHitPoint:
        if playerTurn: playerHP -= 1
    
    if playerHP <= 0: return None
    
    newActiveSpells = []
    for activeSpell in activeSpells:
        if activeSpell.turns >= 0:
            bossHP -= activeSpell.damage
            playerHP += activeSpell.heal
            playerArmor += activeSpell.armor
            playerMana += activeSpell.mana
        newActiveSpell = deepcopy(activeSpell)
        newActiveSpell.turns -= 1
        if newActiveSpell.turns > 0:
            newActiveSpells.append(newActiveSpell)
    
    if bossHP <= 0:
        cheapest = min(manaUsed, cheapest)
        return cheapest
        
    if manaUsed >= cheapest: return None
    
    if playerTurn:
        for i in range(len(spells)):
            sp = spells[i]
            spellAlreadyActive = False
            for j in range(len(newActiveSpells)):
                if newActiveSpells[j].name == sp.name:
                    spellAlreadyActive = True
                    break
                
            if sp.cost <= playerMana and not spellAlreadyActive:
                a = deepcopy(newActiveSpells)
                a.append(sp)
                score = play(bossHP, playerHP, playerMana - sp.cost, a, False, manaUsed + sp.cost, loseHitPoint, cheapest)
                if score:
                    cheapest = min(cheapest, score)
    else:
        playerHP -= max(1, bossDmg - playerArmor)
        if playerHP > 0:
            score = play(bossHP, playerHP, playerMana, newActiveSpells, True, manaUsed, loseHitPoint, cheapest)
            if score:
                cheapest = min(score, cheapest)
            
    return cheapest
        
part1 = play(51, 50, 500, [], True, 0)
part2 = play(51, 50, 500, [], True, 0, loseHitPoint = True)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
