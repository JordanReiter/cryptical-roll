from unittest import TestCase

from crypt_roll.utils import parse_roll

class TestParse(TestCase):
    def test_simple_d6(self):
        result = parse_roll('d6')
        self.assertEqual(result, [6])

    def test_simple_d8(self):
        result = parse_roll('d8')
        self.assertEqual(result, [8])

    def test_simple_d20(self):
        result = parse_roll('d20')
        self.assertEqual(result, [20])
    
    def test_multiple_dice_d6(self):
        result = parse_roll('2d6')
        self.assertEqual(result, [6, 6])
    
    def test_multiple_dice_4d10(self):
        result = parse_roll('4d10')
        self.assertEqual(result, [10, 10, 10, 10])
