import random
import time

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
    
    
    def fight_round(self, other):
        self_damage = self.damage()
        other_damage = other.damage()
        if self_damage > other.shield:
            other.change_health(other.shield - self_damage)
            other.shield = 0
        else:
            other.change_shield(-self_damage)
        if other_damage > self.shield:
            self.change_health(self.shield - other_damage)
            self.shield = 0
        else:
            self.change_shield(-other_damage)

        
    def __str__(self) -> str:
        shield_percentage = round(self.shield / self.max_shield * 100, 2)
        return(f"Health of your ship is: {self.health}, current shield is on {shield_percentage}% level - {self.shield}")
    

if __name__ == "__main__":
    # p = Battlestar(40, 20, 2, 10)
    # print(p.attack)
    # dices = p.roll_attack()
    # print(dices)
    # p.change_health(-30)
    # print(p.health)
    # print(p.is_dead())
    # p.change_health(-30)
    # print(p.health)
    # print(p.is_dead())
    # print(Battlestar.hit(dices))
    # print(p.damage())
    p1 = Battlestar(40, 20, 2, 15)
    p2 = Battlestar(40, 20, 3, 12)
    i = 1
    while p1.health == p1.max_health and p2.health == p2.max_health:
        
        print(f'____________Round {i}__________________')
        
        p1.fight_round(p2)
        p1.change_shield(p1.regeneration)
        p2.change_shield(p2.regeneration)
        print(p1)
        print(p2)

        i += 1
        time.sleep(3)

    while not p1.is_dead() and not p2.is_dead():
        
        print(f'____________Round {i}__________________')
        
        p1.fight_round(p2)
        p1.change_shield(p1.regeneration)
        p2.change_shield(p2.regeneration)
        print(p1)
        print(p2)

        i += 1
        time.sleep(3)