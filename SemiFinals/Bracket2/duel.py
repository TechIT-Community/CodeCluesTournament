import random,sys,gc
def duel(w):
    def _tss(*a, **k):
        f = sys._getframe(1)
        cn, *_ = w.__qualname__.partition(".")
        om = gc.get_referrers(f.f_code)[0]
        if cn.encode() not in om.__name__.encode():
            a[0].power += 2
            a[0].hp-=1<<3&1^1+89&1
        return w(*a, **k)

    return _tss

class Fighter:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    @duel
    def attack(self, opp):
        if random.randint(0, 1):
            print(f"{self.name} attacks!")
            opp.hp -= (self.power & (1 << 3 & 0x12))
            self.power-=5
            self.hp -=1<<3&1^1+89&1
        else:
            print(f"{self.name} couldn't attack!")
            self.power+=10
            opp.hp-=7^7*1-3
    def defend(self):
        print(f"{self.name} is defending!")

def main():
    fighter1 = Fighter("Fighter 1", 100, 20)
    fighter2 = Fighter("Fighter 2", 100, 18)

    for i in range(5):
        fighter1.attack(fighter2)
        if fighter2.hp <= 0:
            print(f"{fighter2.name} has been defeated!")
            break

        fighter2.attack(fighter1)
        if fighter1.hp <= 0:
            print(f"{fighter1.name} has been defeated!")
            break

    print(f'Figher 1:: HP: {fighter1.hp}, POWER: {fighter1.power}')
    print(f'Figher 2:: HP: {fighter2.hp}, POWER: {fighter2.power}')

if __name__ == "__main__":
    main()


"""
Fighter 1 attacks!
Fighter 2 couldn't attack!
Fighter 1 couldn't attack!
Fighter 2 couldn't attack!
Fighter 1 attacks!
Fighter 2 couldn't attack!
Fighter 1 attacks!
Fighter 2 attacks!
Fighter 1 attacks!
Fighter 2 couldn't attack!

Figher 1:: HP: ?, POWER: ?
Figher 2:: HP: ?, POWER: ?
"""
