import unittest
from main import Battlestar

class Test(unittest.TestCase):

    def test_init(self):
        "should return 40, 20, 2 and 10"
        p = Battlestar('star1', 40, 20, 2, 10)
        self.assertEqual(p.attack, 10)
        self.assertEqual(p.health, 40)
        self.assertEqual(p.regeneration, 2)
        self.assertEqual(p.shield, 20)


    def test_roll_attack(self):
        "list of data from 1 to 6 with length of attack"
        p = Battlestar('star1', 40, 20, 2, 30)
        count = 0
        for el in p.roll_attack():
            count += 1
            self.assertLessEqual(el, 6)
            self.assertGreaterEqual(el, 1)
        self.assertEqual(count, 30)

    def test_change_health(self):
        "not more than max health, 40 - 10 = 30, 30 + 20 = 40, 40 - 50 = 0"
        p = Battlestar('star1', 40, 20, 2, 10)
        p.change_health(-10)
        self.assertEqual(p.health, 30)
        p.change_health(20)
        self.assertEqual(p.health, 40)
        p.change_health(-50)
        self.assertEqual(p.health, 0)


    def test_change_shield(self):
        "not more than max shield, 20 - 10 = 10, 10 + 20 = 20, 20 - 50 = 0"
        p = Battlestar('star1', 40, 20, 2, 10)
        p.change_shield(-10)
        self.assertEqual(p.shield, 10)
        p.change_shield(20)
        self.assertEqual(p.shield, 20)
        p.change_shield(-50)
        self.assertEqual(p.shield, 0)


    def test_is_dead(self):
        "20 health is not dead, 0 - is dead"
        p = Battlestar('star1', 40, 20, 2, 10)
        p.change_health(-20)
        self.assertFalse(p.is_dead())
        p.change_health(-30)
        self.assertTrue(p.is_dead())


    def test_hit(self):
        "sum of all cases >=  Base accuracy (5)"
        self.assertEqual(Battlestar.hit([1,2,3,4,5,6]), 2)

    
    def test_damage(self):
        "run 10000 rounds of attach and calculate damage:) - in average it should be 1/3 and alpha = 99% (diff < 0.01)"
        p = Battlestar('star1', 40, 20, 2, 30)
        res = 0
        for i in range(10000):
            res += p.damage()
        res /= 100000
        print(abs(res - 1))
        self.assertLess(abs(res - 1), 0.01)

if __name__ == "__main__":
    unittest.main()