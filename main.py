import random

class Battlestar():
    
    MAX_CRIT = 10
    BASE_ACCURACY = 5

    def __init__(self, health, shield, regeneration, attack):
        self.health = health
        self.max_health = health
        self.shield = shield
        self.max_shield = shield
        self.regeneration = regeneration
        self.attack = attack
        self.accuracy = Battlestar.BASE_ACCURACY
        self.crit = 0


    def roll_attack(self):
        return [random.randint(1, 6) for i in range(self.attack)]
    
 
    def change_health(self, quantity):
        self.health = max(0, self.health + quantity)
        self.health = min(self.max_health, self.health)
    
 
    def change_shield(self, quantity):
        self.shield = max(0, self.shield + quantity)
        self.shield = min(self.max_shield, self.shield)
    
 
    def is_dead(self):
        if self.health == 0:
            return True
        return False

    @classmethod
    def hit(self, dices:list):
        return sum([dice >= Battlestar.BASE_ACCURACY for dice in dices])
    

    def damage(self):
        return Battlestar.hit(self.roll_attack())
    

if __name__ == "__main__":
    p = Battlestar(40, 20, 2, 10)
    print(p.attack)
    dices = p.roll_attack()
    print(dices)
    p.change_health(-30)
    print(p.health)
    print(p.is_dead())
    p.change_health(-30)
    print(p.health)
    print(p.is_dead())
    print(Battlestar.hit(dices))
    print('check damage')
    for i in range(10):
        print(p.damage())