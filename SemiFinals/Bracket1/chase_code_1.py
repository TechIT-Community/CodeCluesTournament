import time
import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.debuff = 0

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        time.sleep(2)
        damage = max(0, self.attack_power - target.debuff)
        target.take_damage(damage)

    def take_damage(self, damage):
        print(f"{self.name} takes {damage} damage!")
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)
        self.blocked_last_turn = False

    def slash(self, target):
        print(f"{self.name} wields a mysterious blade, slashing {target.name}!")
        time.sleep(2)
        damage = max(0, self.attack_power + 15 - target.debuff)
        target.take_damage(damage)

    def block(self):
        print(f"{self.name} activates a magical shield, preparing for the unknown!")
        time.sleep(2)
        self.debuff += 10
        self.blocked_last_turn = True

    def reset_block(self):
        self.blocked_last_turn = False

class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)
        self.enchanted_last_turn = False

    def cast_spell(self, target):
        print(f"{self.name} conjures a spell, aiming it at {target.name}!")
        time.sleep(3)
        damage = max(0, self.attack_power + 20 - target.debuff)
        target.take_damage(damage)

    def enchant(self, target):
        print(f"{self.name} enchants the surroundings, empowering {target.name}!")
        time.sleep(2)
        target.debuff += 5
        self.enchanted_last_turn = True

    def reset_enchant(self):
        self.enchanted_last_turn = False

class MysteriousEntity(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

class AdventureArena:
    def __init__(self):
        self.characters = []
        self.entities_defeated = 0

    def add_character(self, character):
        self.characters.append(character)

    def start_adventure(self):
        print("An ancient mystery unfolds!")
        time.sleep(1)
        for turn in range(5):  # Embrace the uncertainty in 5 turns
            print(f"\nTurn {turn + 1}:")
            for character in self.characters:
                if isinstance(character, Hero):
                    if random.choice([True, False]):
                        target = self.get_random_target(character)
                        character.slash(target)
                    else:
                        character.block()
                elif isinstance(character, Sorcerer):
                    if random.choice([True, False]):
                        target = self.get_random_target(character)
                        character.cast_spell(target)
                    else:
                        ally = self.get_random_ally(character)
                        character.enchant(ally)

            self.reset_actions()


    def get_random_target(self, attacker):
        targets = [c for c in self.characters if isinstance(c, Character) and c != attacker and c.health > 0]
        return random.choice(targets)

    def get_random_ally(self, caster):
        allies = [c for c in self.characters if isinstance(c, Character) and c != caster and c.health > 0]
        return random.choice(allies)

    def reset_actions(self):
        for character in self.characters:
            if isinstance(character, Hero):
                character.reset_block()
            elif isinstance(character, Sorcerer):
                character.reset_enchant()

# Object creation and embark on the mysterious adventure
adventure_arena = AdventureArena()

hero = Hero("BraveHero")
sorcerer = Sorcerer("MysticSorcerer")
entity1 = MysteriousEntity("MysteriousEntity1", health=100, attack_power=30)
entity2 = MysteriousEntity("MysteriousEntity2", health=80, attack_power=40)
entity3 = MysteriousEntity("MysteriousEntity3", health=70, attack_power=30)
entity4 = MysteriousEntity("MysteriousEntity4", health=90, attack_power=22)
entity5 = MysteriousEntity("MysteriousEntity5", health=60, attack_power=28)

adventure_arena.add_character(hero)
adventure_arena.add_character(sorcerer)
adventure_arena.add_character(entity1)
adventure_arena.add_character(entity2)
adventure_arena.add_character(entity3)
adventure_arena.add_character(entity4)
adventure_arena.add_character(entity5)

# Begin the mysterious adventure
adventure_arena.start_adventure()

"""
An ancient mystery unfolds!

Turn 1:
BraveHero activates a magical shield, preparing for the unknown!
MysticSorcerer enchants the surroundings, empowering MysteriousEntity5!

Turn 2:
BraveHero wields a mysterious blade, slashing MysteriousEntity3!
MysteriousEntity3 takes 40 damage!
MysticSorcerer conjures a spell, aiming it at MysteriousEntity4!
MysteriousEntity4 takes 50 damage!

Turn 3:
BraveHero wields a mysterious blade, slashing MysteriousEntity3!
MysteriousEntity3 takes 40 damage!
MysteriousEntity3 has been defeated!
MysticSorcerer enchants the surroundings, empowering MysteriousEntity4!

Turn 4:
BraveHero wields a mysterious blade, slashing MysteriousEntity1!
MysteriousEntity1 takes 40 damage!
MysticSorcerer enchants the surroundings, empowering MysteriousEntity2!

Turn 5:
BraveHero activates a magical shield, preparing for the unknown!
MysticSorcerer conjures a spell, aiming it at MysteriousEntity4!
MysteriousEntity4 takes 45 damage!


# Find the number of mysterious entities defeated at the end of the adventure.
"""


