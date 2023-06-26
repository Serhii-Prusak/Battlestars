import random
import time
import json
import pprint


def balance_parameters_ships(n=100):
        ship = lambda i: (data['ships'][i]['name'], data['ships'][i]['health'], data['ships'][i]['shield'], data['ships'][i]['regeneration'], data['ships'][i]['attack'])
        total_dict = {}
        for s in range(len(data['ships'])):
            total_dict[s] = []    
            for op in range(len(data['ships'])):
                total_dict[s].append(0)
                if op == s:
                    continue
                res = [0, 0] 
                for i in range(n):
                    p1 = Battlestar(*ship(s))
                    p2 = Battlestar(*ship(op))
                    while not p1.is_dead() and not p2.is_dead():
                        p1.fight_round(p2)
                        p1.change_shield(p1.regeneration)
                        p2.change_shield(p2.regeneration)
                    res[0] += int(not p1.is_dead()) + int(p2.is_dead())
                    res[1] += int(not p2.is_dead()) + int(p1.is_dead())
                total_dict[s][-1] += res[0] - n
                # print('result is: ', res, 'for', p2.max_health + p2.max_shield)
        for el in sorted(total_dict, key=lambda x: sum(total_dict[x]), reverse=True):
            print(f"Ship {el:2} - {data['ships'][el]['name'][-7:]} has {sum(total_dict[el])/n:=+6.2f}")

            
class Battlestar():
    
    MAX_CRIT = 10
    BASE_ACCURACY = 5

    def __init__(self, name, health, shield, regeneration, attack):
        self.name = name
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
        shield_percentage = round(self.shield / self.max_shield * 100, 2) if self.max_shield else 0
        return(f"Health of your ship is: {self.health}, current shield is on {shield_percentage}% level - {self.shield}")
    

if __name__ == "__main__":

    start = time.time()

    with open('ships.json', 'r') as f:
        data = json.load(f)

    balance_parameters_ships(100)
    # p1 = Battlestar(10, 35, 3, 20)
    # p2 = Battlestar(35, 22, 1, 19)
    # i = 1
    # while p1.health == p1.max_health and p2.health == p2.max_health:
        
    #     print(f'____________Round {i}__________________')
        
    #     p1.fight_round(p2)
    #     p1.change_shield(p1.regeneration)
    #     p2.change_shield(p2.regeneration)
    #     print(p1)
    #     print(p2)

    #     i += 1
    #     time.sleep(2)

    # while not p1.is_dead() and not p2.is_dead():
        
    #     print(f'____________Round {i}__________________')
        
    #     p1.fight_round(p2)
    #     p1.change_shield(p1.regeneration)
    #     p2.change_shield(p2.regeneration)
    #     print(p1)
    #     print(p2)

    #     i += 1
    #     time.sleep(3)
    print(f"Processed time is {time.time() - start} sec")