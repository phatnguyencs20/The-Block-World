from predicate import *
from action import *
import unittest



class TestPredicateArmEmpty(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(ArmEmpty(), ArmEmpty())
        self.assertNotEqual(ArmEmpty(), 1)
        self.assertNotEqual(ArmEmpty(), 'A')
        self.assertNotEqual(ArmEmpty(), OnTop('X', 'Y'))
        self.assertNotEqual(ArmEmpty(), Top('X'))
        self.assertNotEqual(ArmEmpty(), Holding('X'))
        self.assertNotEqual(ArmEmpty(), OnTable('X'))


class TestPredicateHolding(unittest.TestCase):
    def test_equality(self):
        for i in range(ord('A'), ord('Z') + 1):
            self.assertEqual(Holding(chr(i)), Holding(chr(i)))
            self.assertNotEqual(Holding(chr(i)), Top(chr(i)))
            self.assertNotEqual(Holding(chr(i)), ArmEmpty())
            self.assertNotEqual(Holding(chr(i)), OnTable(chr(i)))
            self.assertNotEqual(Holding(chr(i)), i)
            self.assertNotEqual(Holding(chr(i)), chr(i))
            self.assertNotEqual(Holding(chr(i)), OnTop(chr(i), chr((i + 1) % 26 + 65)))
    
    def test_hash(self):
        for i in range(ord('A'), ord('Z') + 1):
            self.assertEqual(hash(Holding(chr(i))), hash(Holding(chr(i))))

class TestPredicateTop(unittest.TestCase):
    def test_equality(self):
        for i in range(ord('A'), ord('Z') + 1):
            self.assertEqual(Top(chr(i)), Top(chr(i)))
            self.assertNotEqual(Top(chr(i)), i)
            self.assertNotEqual(Top(chr(i)), chr(i))
            self.assertNotEqual(Top(chr(i)), Holding(chr(i)))
            self.assertNotEqual(Top(chr(i)), OnTable(chr(i)))
            self.assertNotEqual(Top(chr(i)), ArmEmpty())
            self.assertNotEqual(Top(chr(i)), OnTop(chr(i), chr((i + 1) % 26 + 65)))

    def test_hash(self):
        for i in range(ord('A'), ord('Z') + 1):
            i = chr(i)
            self.assertEqual(hash(Top(i)), hash(Top(i)))

    
if __name__ == '__main__':
    unittest.main(verbosity=2)