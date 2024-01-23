import random
import time
from PIL import Image, ImageDraw, ImageFont

def obfuscate(text):
    mapping = {}
    for char in set(text):
        mapping[char] = chr(random.randint(33, 126))
    obfuscated = "".join(mapping.get(char, char) for char in text)
    return obfuscated

class EnigmaticCharacter:
    def __init__(self, name, role, secrets):
        self.name = name
        self.role = obfuscate(role)
        self.secrets = [obfuscate(secret) for secret in secrets]
        self.image = Image.open(random.choice(["suspect1.jpg", "suspect2.jpg", "suspect3.jpg"]))

    def reveal(self, key):
        if key == self.role:
            self.role = self.role.lower()
        elif key in self.secrets:
            self.secrets.remove(key)
            print("A secret has been revealed...")
        else:
            print("The key does not unlock any secrets.")

characters = [
    EnigmaticCharacter("The Raven", "Guardian", ["Dark past", "Hidden agenda"]),
    EnigmaticCharacter("The Muse", "Trickster", ["Mystical powers", "Unknown motives"]),
    EnigmaticCharacter("The Shadow", "Spy", ["Double life", "Secret society"])
]

def generate_cryptic_message():
    font = ImageFont.truetype("cryptic_font.ttf", 48)
    canvas = Image.new("RGB", (800, 600), color="black")
    draw = ImageDraw.Draw(canvas)

    riddle = "The truth lies beneath the veil of illusion. Seek the key to unlock the hidden paths."
    draw.text((50, 50), obfuscate(riddle), font=font, fill="white")

    return canvas

while True:
    cryptic_message = generate_cryptic_message()
    cryptic_message.show()

    print("\nThe Enigmatic Characters await your guidance.")
    print("Choose a character to interact with:")
    for i, character in enumerate(characters):
        print(f"{i+1}. {character.name}")

    choice = input("Enter your choice (1-3): ")
    if choice in ["1", "2", "3"]:
        chosen_character = characters[int(choice) - 1]

        chosen_character.image.show()

        key = input("Enter a key to unlock their secrets: ")
        chosen_character.reveal(key)

        if all(secret == "" for character in characters for secret in character.secrets):
            print("\nCongratulations! You have unraveled all the mysteries.")
            break
    else:
        print("Invalid choice. Please try again.")

    time.sleep(2)

"""
    Space battle begins!

Turn 1:
SpaceStation1 fires its laser at Alien1!
Alien1 takes 15 damage!
Alien1 evades the attack!
Alien2 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien3 attempts to abduct Alien2!
Alien2 takes 35 damage!
Alien4 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien5 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!

Turn 2:
SpaceStation1 fires its laser at Alien1!
Alien1 takes 15 damage!
Alien1 evades the attack!
Alien2 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien3 evades the attack!
Alien4 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien5 attempts to abduct Alien2!
Alien2 takes 35 damage!

Turn 3:
SpaceStation1 initiates repairs!
Alien1 evades the attack!
Alien2 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien3 evades the attack!
Alien4 attempts to abduct Alien5!
Alien5 takes 35 damage!
Alien5 evades the attack!

Turn 4:
SpaceStation1 initiates repairs!
Alien1 evades the attack!
Alien2 evades the attack!
Alien3 evades the attack!
Alien4 evades the attack!
Alien5 attempts to abduct Alien1!
Alien1 takes 35 damage!

Turn 5:
SpaceStation1 fires its laser at Alien4!
Alien4 takes 15 damage!
Alien1 attempts to abduct Alien3!
Alien3 takes 35 damage!
Alien2 attempts to abduct Alien3!
Alien3 takes 35 damage!
Alien3 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien4 attempts to abduct Alien2!
Alien2 takes 35 damage!
Alien5 attempts to abduct Alien3!
Alien3 takes 35 damage!

Question for opponents: What is 5 * 3?
Enter your answer: 15
Correct! You successfully answered the question.
Number of aliens defeated: 0

  │  ~/De/temp  python -u "/Users/chiran/Desktop/temp/cc.py"                      ✔ │ took 2m 42s  │ base  │ at 04:36:44 PM  
Space battle begins!

Turn 1:
SpaceStation1 fires its laser at Alien5!
Alien5 takes 15 damage!
Alien1 attempts to abduct Alien5!
Alien5 takes 35 damage!
Alien2 evades the attack!
Alien3 attempts to abduct Alien2!
Alien2 takes 35 damage!
Alien4 attempts to abduct Alien1!
Alien1 takes 35 damage!
Alien5 evades the attack!

Turn 2:
SpaceStation1 initiates repairs!
Alien1 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien2 attempts to abduct Alien1!
Alien1 takes 35 damage!
Alien3 attempts to abduct Alien5!
Alien5 takes 35 damage!
Alien4 attempts to abduct Alien2!
Alien2 takes 35 damage!
Alien5 attempts to abduct Alien4!
Alien4 takes 35 damage!

Turn 3:
SpaceStation1 fires its laser at Alien2!
Alien2 takes 15 damage!
Alien1 attempts to abduct Alien2!
Alien2 takes 35 damage!
Alien2 evades the attack!
Alien3 attempts to abduct Alien5!
Alien5 takes 35 damage!
Alien4 evades the attack!
Alien5 evades the attack!

Turn 4:
SpaceStation1 initiates repairs!
Alien1 attempts to abduct Alien2!
Alien2 takes 35 damage!
Alien2 has been disabled!
Alien2 evades the attack!
Alien3 attempts to abduct Alien1!
Alien1 takes 35 damage!
Alien4 attempts to abduct Alien3!
Alien3 takes 35 damage!
Alien5 evades the attack!

Turn 5:
SpaceStation1 initiates repairs!
Alien1 evades the attack!
Alien2 evades the attack!
Alien3 attempts to abduct SpaceStation1!
SpaceStation1 takes 35 damage!
Alien4 evades the attack!
Alien5 evades the attack!


Question what is the health of Alien1,3,5 ?
"""