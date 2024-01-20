#find the murderer.
import time

class Person:
    def __init__(self, name, occupation, alibi, suspicion_level=0):
        self.name = name
        self.occupation = occupation
        self.alibi = alibi
        self.suspicion_level = suspicion_level
        self.suspicious_behavior = False

    def talk(self):
        return f"{self.name}, a {self.occupation}, says: Hello, I was {self.alibi} during the time of the incident."

    def increase_suspicion(self, attribute, value, motive_effect=0, skill_effect=0):
        print(f"{self.name} exhibits suspicious behavior: {attribute}!")
        self.suspicion_level += value
        self.suspicion_level += motive_effect  # Increase suspicion based on motive effect
        self.suspicion_level += skill_effect   # Increase suspicion based on skill effect
        self.suspicious_behavior = True

    def display_attributes(self):
        pass  # To be implemented in subclasses

class Detective(Person):
    def __init__(self, name):
        super().__init__(name, "Detective", "investigating the crime scene")
        self.analysis_skill = 12

    def investigate(self, attribute, value):
        print(f"{self.name} investigates the crime scene and finds evidence: {attribute}!")
        self.suspicion_level -= value

    def analyze_evidence(self, evidence, value):
        print(f"{self.name} analyzes the evidence: {evidence}")
        self.suspicion_level -= value

    def display_attributes(self):
        print(f"{self.name} has analysis skill level: {self.analysis_skill}")

class Witness(Person):
    def __init__(self, name):
        super().__init__(name, "Witness", "seeing the incident")
        self.memory_skill = 10

    def provide_testimony(self, value):
        print(f"{self.name} witnessed the incident and provides a testimony.")
        self.suspicion_level -= value

    def display_attributes(self):
        print(f"{self.name} has memory skill level: {self.memory_skill}")

class Suspect(Person):
    def __init__(self, name, occupation, alibi, suspicion_level=0):
        super().__init__(name, occupation, alibi, suspicion_level)
        self.deception_skill = 8
        self.motive = f"{self.name}'s motive: revenge"
        self.motive_skill = 9
        self.opportunity_skill = 7
        self.behavior_skill = 6
        self.alibi_consistency = 8

    def talk(self):
        return f"{self.name}, a {self.occupation}, says: I was {self.alibi}. You can't prove otherwise."

    def display_attributes(self):
        print(f"{self.name} has deception skill level: {self.deception_skill}")
        print(f"{self.motive}")
        print(f"{self.name}'s opportunity skill level: {self.opportunity_skill}")
        print(f"{self.name}'s behavior skill level: {self.behavior_skill}")
        print(f"{self.name}'s alibi consistency level: {self.alibi_consistency}")

    def increase_suspicion(self, attribute, value, motive_effect=0, skill_effect=0):
        super().increase_suspicion(attribute, value, motive_effect, skill_effect)
        self.suspicion_level += self.deception_skill * skill_effect  # Adjust suspicion based on skill
        self.suspicion_level += self.motive_skill * motive_effect 

class CrimeScene:
    def __init__(self, location, time_of_incident, victim):
        self.location = location
        self.time_of_incident = time_of_incident
        self.victim = victim
        self.murder_weapon = MurderWeapon("Bloody Knife", "lethal")

    def investigate(self, detectives, suspects, witnesses):
        print(f"\nInvestigating the crime scene at {self.location}...")
        print(f"The incident occurred at {self.time_of_incident}. The victim is {self.victim}.")
        print(f"A murder weapon, a {self.murder_weapon.description}, was found.")

        for detective in detectives:
            detective.investigate("found near the crime scene", 10)
            detective.analyze_evidence(self.murder_weapon.description, 8)
            detective.display_attributes()

        for witness in witnesses:
            witness.provide_testimony(5)
            witness.display_attributes()

        for suspect in suspects:
            print("\n" + "-"*40)
            print(suspect.talk())
            suspect.display_attributes()

            if not suspect.suspicious_behavior:
                print(f"{suspect.name} seems innocent for now.")


class Suspect2(Person):
    def __init__(self, name, occupation, alibi, suspicion_level=0):
        super().__init__(name, occupation, alibi, suspicion_level)
        self.deception_skill = 7
        self.motive = f"{self.name}'s motive: unknown"
        self.motive_skill = 8
        self.opportunity_skill = 6
        self.behavior_skill = 5
        self.alibi_consistency = 7

    def talk(self):
        return f"{self.name}, a {self.occupation}, says: I was {self.alibi}. It's none of your business."

    def display_attributes(self):
        print(f"{self.name} has deception skill level: {self.deception_skill}")
        print(f"{self.motive}")
        print(f"{self.name}'s opportunity skill level: {self.opportunity_skill}")
        print(f"{self.name}'s behavior skill level: {self.behavior_skill}")
        print(f"{self.name}'s alibi consistency level: {self.alibi_consistency}")

def solve_murder_mystery():
    detective1 = Detective("Detective Holmes")
    detective2 = Detective("Detective Watson")

    alice = Witness("Alice")
    bob = Suspect("Bob", "Businessman", "attending a meeting", suspicion_level=10)
    charlie = Suspect("Charlie", "Actor", "rehearsing lines", suspicion_level=8)
    david = Suspect("David", "Journalist", "writing an article", suspicion_level=5)
    jugujugu = Suspect2("Jugujugu", "Unknown", "nowhere to be found", suspicion_level=12)
    bujubuju = Suspect2("Bujubuju", "Mysterious Figure", "in the shadows", suspicion_level=15)

    crime_scene = CrimeScene("Mystery Mansion", "9:00 PM", "Mr. Smith")

    detectives = [detective1, detective2]
    suspects = [bob, charlie, david, jugujugu, bujubuju]
    witnesses = [alice]

    for _ in range(3):  # Simulate multiple rounds of investigation for demonstration purposes
        crime_scene.investigate(detectives, suspects, witnesses)
        print("\nAnalyzing Motives...")
        motive_analysis(detectives, suspects)

        print("\nFinal Suspicion Level for Each Suspect:")
        for suspect in suspects:
            print(f"{suspect.name}: {suspect.suspicion_level}")

        print("\nBased on the suspicion level, who's the murderer?")
        find_murderer(suspects)

def motive_analysis(detectives, suspects):
    for detective in detectives:
        print(f"\n{detective.name} analyzes the motives...")
        for suspect in suspects:
            print(f"{suspect.name}'s motive skill level: {suspect.motive_skill}")
            detective.suspicion_level -= suspect.motive_skill

def find_murderer(suspects):
    max_suspicion = max(suspects, key=lambda x: x.suspicion_level)
    print(f"The murderer is {max_suspicion.name}!")

class MurderWeapon:
    def __init__(self, description, lethality):
        self.description = description
        self.lethality = lethality

def main():
    solve_murder_mystery()

if __name__ == "__main__":
    main()
