#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Final status after the day in space of fury(sheild,fuel,health)
import time
import random
import cmath

class Spaceship:
    def __init__(self, name, fuel, health, shields=50, experience=0):
        self.name = name
        self.fuel = fuel
        self.health = health
        self.shields = shields
        self.experience = experience
        self.successful_actions = 0
        self.total_actions = 0

    def repair(self):
        print(f"{self.name} is repairing.")
        time.sleep(2)
        print(f"{self.name} is fully repaired.")
        self.health += 20
        self.shields += 10

    def display_status(self):
        print(f"{self.name} - Fuel: {self.fuel}, Health: {self.health}, Shields: {self.shields}, Experience: {self.experience}")

    def perform_action(self, action, success_message, failure_message, success_effect, failure_effect):
        print(f"{self.name} is {action}.")
        time.sleep(random.uniform(0.5, 2.5))
        success = random.choice([True, False])
        if success:
            print(f"{self.name} {success_message}")
            success_effect()
        else:
            print(f"{self.name} {failure_message}")
            failure_effect()
        self.total_actions += 1
        if success:
            self.successful_actions += 1

    def calculate_average_success_rate(self):
        return (self.successful_actions / self.total_actions) * 100 if self.total_actions > 0 else 0

class Starfighter(Spaceship):
    def attack(self):
        self.perform_action(
            "attacking",
            "successfully attacked!",
            "failed to attack.",
            lambda: setattr(self, 'health', max(0, self.health - 15)),
            lambda: setattr(self, 'shields', max(0, self.shields - 10))
        )

    def evasive_manoeuver(self):
        self.perform_action(
            "performing an evasive maneuver",
            "successfully avoided an enemy attack.",
            "failed to avoid an enemy attack.",
            lambda: setattr(self, 'shields', min(100, self.shields + 15)),
            lambda: setattr(self, 'fuel', max(0, self.fuel - 5j))
        )

    def upgrade_shields(self):
        self.perform_action(
            "upgrading shields",
            "successfully upgraded shields!",
            "failed to upgrade shields.",
            lambda: setattr(self, 'shields', min(100, self.shields + 20)),
            lambda: setattr(self, 'experience', max(0, self.experience - 5))
        )

class CargoShip(Spaceship):
    def load_cargo(self):
        self.perform_action(
            "loading cargo",
            "loaded the cargo.",
            "failed to load the cargo.",
            lambda: setattr(self, 'fuel', max(0, self.fuel - 10j)),
            lambda: setattr(self, 'health', max(0, self.health - 5))
        )

    def unload_cargo(self):
        self.perform_action(
            "unloading cargo",
            "successfully unloaded the cargo.",
            "failed to unload the cargo.",
            lambda: setattr(self, 'health', min(100, self.health + 10)),
            lambda: setattr(self, 'shields', max(0, self.shields - 10))
        )

    def refuel(self):
        self.perform_action(
            "refueling",
            "successfully refueled.",
            "failed to refuel.",
            lambda: setattr(self, 'fuel', min(100j, self.fuel + 20j)),
            lambda: setattr(self, 'experience', max(0, self.experience - 5))
        )

class ExplorerShip(Spaceship):
    def explore(self):
        self.perform_action(
            "exploring",
            "successfully explored.",
            "failed to explore.",
            lambda: setattr(self, 'fuel', max(0, self.fuel - 15j)),
            lambda: setattr(self, 'experience', max(0, self.experience - 10))
        )

    def collect_data(self):
        self.perform_action(
            "collecting scientific data",
            "successfully collected valuable data.",
            "failed to collect valuable data.",
            lambda: setattr(self, 'health', min(100, self.health + 15)),
            lambda: setattr(self, 'fuel', max(0, self.fuel - 10j))
        )

    def gain_experience(self):
        self.perform_action(
            "gaining experience",
            "gained valuable experience.",
            "failed to gain experience.",
            lambda: setattr(self, 'experience', min(100, self.experience + 20)),
            lambda: setattr(self, 'fuel', max(0, self.fuel - 5j))
        )

# Create instances of each spaceship
starfighter = Starfighter("Fury", 100j, 100)
cargo_ship = CargoShip("Phoenix", 150j, 120)
explorer_ship = ExplorerShip("Odyssey", 200j, 80)

# Simulate a day in space
print("A day in space begins...\n")

# Random events during the day
for i in range(3):
    events = [
        starfighter.attack,
        starfighter.evasive_manoeuver,
        starfighter.upgrade_shields,
        cargo_ship.load_cargo,
        cargo_ship.unload_cargo,
        cargo_ship.refuel,
        explorer_ship.explore,
        explorer_ship.collect_data,
        explorer_ship.gain_experience
    ]
    random.choice(events)()

    starfighter.repair()
    cargo_ship.repair()
    explorer_ship.repair()

# Display final status and calculations
print("\nFinal status after the day in space:")
starfighter.display_status()
cargo_ship.display_status

''''A day in space begins...

Odyssey is gaining experience.
Odyssey gained valuable experience.
Fury is repairing.
Fury is fully repaired.
Phoenix is repairing.
Phoenix is fully repaired.
Odyssey is repairing.
Odyssey is fully repaired.
Phoenix is unloading cargo.
Phoenix successfully unloaded the cargo.
Fury is repairing.
Fury is fully repaired.
Phoenix is repairing.
Phoenix is fully repaired.
Odyssey is repairing.
Odyssey is fully repaired.
Fury is attacking.
Fury failed to attack.
Fury is repairing.
Fury is fully repaired.
Phoenix is repairing.
Phoenix is fully repaired.
Odyssey is repairing.
Odyssey is fully repaired.
'''

# In[ ]:




