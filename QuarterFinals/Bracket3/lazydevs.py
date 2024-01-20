class Warrior:
    def __init__(self, name, role, health):
        self.name = name
        self.role = role
        self.health = health
    def attack(self):
        print(f"{self.role} {self.name} launches an attack.")
    def defend(self):
        print(f"{self.role} {self.name} defends against enemy attacks.")
    def victory_dance(self):
        print(f"{self.role} {self.name} celebrates the victory with a triumphant dance!")

class King(Warrior):
    def __init__(self, name, health):
        super().__init__(name, "King", health)
    def rule_kingdom(self):
        print(f"King {self.name} is ruling the kingdom wisely.")
        print(f"King {self.name} ensures the prosperity of the kingdom.")
    def lead_army(self):
        print(f"King {self.name} is leading the army into battle.")
        print(f"King {self.name} inspires the army to fight bravely.")
        self.health -= 5
    def defend(self):
        print(f"King {self.name} defends the kingdom from enemy attacks.")
        print(f"King {self.name} ensures the safety of the kingdom.")
        self.health += 3

    def __mul__(self, other):
        self.health+=other.health*3

    def __sub__(self, other):
        self*other
    def engage_in_duel(self, opponent):
        print(f"King {self.name} challenges King {opponent.name} to a duel!")
        print(f"The duel begins...")

        self.attack()
        opponent.defend()

        self-opponent

        if self.health > opponent.health:
            print(f"King {self.name} wins the duel against King {opponent.name}!")
        elif self.health < opponent.health:
            print(f"King {opponent.name} wins the duel against King {self.name}!")
        else:
            print(f"The duel between King {self.name} and King {opponent.name} ends in a draw!")
class Army(Warrior):
    def __init__(self, name, health):
        super().__init__(name, "Army", health)

    def march(self):
        print(f"The army is marching towards the enemy lines.")
        print(f"The army is in position, ready for battle.")

    def charge(self):
        print(f"The army charges forward with full force.")
        print(f"The enemy is overwhelmed by the powerful charge.")
        self.health += 15

    def attack(self):
        print(f"The army launches a coordinated attack on the enemy.")
        print(f"The enemy is defeated by the mighty army.")
        self.health += 10

class Chariot(Warrior):
    def __init__(self, name, health):
       super().__init__(name, "Chariot", health)

    def deploy(self):
        print(f"The chariot, driven by {self.name}, is deployed for battle.")
        print(f"The chariot moves swiftly on the battleground.")
        self.health -= 3
    def shoot_arrows(self):
        print(f"The chariot shoots a volley of arrows at the enemy.")
        print(f"The enemy is pinned down by the accurate arrow shots.")
        self.health += 8

    def ram(self):
        print(f"The chariot rams into the enemy lines, causing chaos.")
        print(f"The enemy forces are scattered by the chariot's impact.")
        self.health += 8


# Create instances of warriors and units
king1 = King("Arthur", 100)
king2 = King("Richard", 100)
army = Army("Red Legion", 200)
chariot = Chariot("Thunderbolt", 50)

# Battleground actions
print("The epic battle begins...")

king1.rule_kingdom()
king1.lead_army()
army.march()
chariot.deploy()
army.charge()
chariot.shoot_arrows()
king1.defend()
army.attack()
chariot.ram()
king1.lead_army()

# Engage in a duel between the two kings
king1.engage_in_duel(king2)

# Print the health of each warrior after the battle
print("\nHealth levels after the battle:")
print(f"King {king1.name}: {king1.health}")
print(f"King {king2.name}: {king2.health}")
print(f"Army {army.name}: {army.health}")
print(f"Chariot {chariot.name}: {chariot.health}")

# Victory dance
king1.victory_dance()
king2.victory_dance()
army.victory_dance()
chariot.victory_dance()


'''
The epic battle begins...
King Arthur is ruling the kingdom wisely.
King Arthur ensures the prosperity of the kingdom.
King Arthur is leading the army into battle.
King Arthur inspires the army to fight bravely.
The army is marching towards the enemy lines.
The army is in position, ready for battle.
The chariot, driven by Thunderbolt, is deployed for battle.
The chariot moves swiftly on the battleground.
The army charges forward with full force.
The enemy is overwhelmed by the powerful charge.
The chariot shoots a volley of arrows at the enemy.
The enemy is pinned down by the accurate arrow shots.
King Arthur defends the kingdom from enemy attacks.
King Arthur ensures the safety of the kingdom.
The army launches a coordinated attack on the enemy.
The enemy is defeated by the mighty army.
The chariot rams into the enemy lines, causing chaos.
The enemy forces are scattered by the chariot's impact.
King Arthur is leading the army into battle.
King Arthur inspires the army to fight bravely.
King Arthur challenges King Richard to a duel!
The duel begins...
King Arthur launches an attack.
King Richard defends the kingdom from enemy attacks.
King Richard ensures the safety of the kingdom.
King Arthur wins the duel against King Richard!

Health levels after the battle:
King Arthur: 
King Richard: 
Army Red Legion: 
Chariot Thunderbolt: 
King Arthur celebrates the victory with a triumphant dance!
King Richard celebrates the victory with a triumphant dance!
Army Red Legion celebrates the victory with a triumphant dance!
Chariot Thunderbolt celebrates the victory with a triumphant dance!
'''
