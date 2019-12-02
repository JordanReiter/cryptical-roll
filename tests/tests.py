from unittest import TestCase, mock

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

    def test_simple_d6_modifier_plus_4(self):
        result = parse_roll('d6+4')
        self.assertEqual(result, ([6], 4))

    def test_simple_d6_modifier_minus_7(self):
        result = parse_roll('d6-7')
        self.assertEqual(result, ([6], -7))

    def test_multiple_dict_3d6_modifier_plus_2(self):
        result = parse_roll('3d6+2')
        self.assertEqual(result, ([6, 6, 6], 2))


class TestRoll(TestCase):
    def test_roll_d6(self):
        expected_value = 3
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import roll_dice
            # function should add one to random value
            m.return_value = expected_value - 1
            output = roll_dice([6])
        self.assertTrue(m.called)
        self.assertEqual(m.call_count, 1)
        self.assertEqual(m.call_args, mock.call(6))
        self.assertEqual(output, [expected_value])

    def test_roll_d8(self):
        expected_value = 7
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import roll_dice
            # function should add one to random value
            m.return_value = expected_value - 1
            output = roll_dice([8])
        self.assertTrue(m.called)
        self.assertEqual(m.call_count, 1)
        self.assertEqual(m.call_args, mock.call(8))
        self.assertEqual(output, [expected_value])

    def test_roll_multiple_dice_4d10_args(self):
        expected_values = [2, 4, 6, 8]
        # function should add one to random value
        # so remove 1 from secrets.randbelow arg
        rand_results = [ val - 1 for val in expected_values]
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import roll_dice
            m.side_effect = rand_results
            output = roll_dice([10, 10, 10, 10])
        self.assertTrue(m.called)
        self.assertEqual(m.call_count, 4)
        expected_calls = [mock.call(10)] * 4
        m.assert_has_calls(expected_calls, any_order=True)
        self.assertEqual(output, expected_values)

    def test_get_roll_result_simple_d6(self):
        dice_type = 6
        expected_value = 2
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import get_roll_result
            # function should add one to random value
            m.return_value = expected_value - 1
            output = get_roll_result([dice_type])
        self.assertTrue(m.called)
        self.assertEqual(m.call_count, 1)
        self.assertEqual(m.call_args, mock.call(dice_type))
        self.assertEqual(output, expected_value)

    def test_get_roll_result_simple_d6_plus_modifier(self):
        dice_type = 6
        modifier = 4
        expected_roll = 2
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import get_roll_result
            # function should add one to random value
            m.return_value = expected_roll - 1
            output = get_roll_result([dice_type], modifier)
        self.assertEqual(output, 6)

    def test_get_roll_result_simple_d6_minus_modifier(self):
        dice_type = 6
        modifier = -1
        expected_roll = 2
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import get_roll_result
            # function should add one to random value
            m.return_value = expected_roll - 1
            output = get_roll_result([dice_type], modifier)
        self.assertEqual(output, 1)

    def test_get_roll_result_multiple(self):
        dice_type = 10
        expected_values = [2, 4, 6, 8]
        # function should add one to random value
        # so remove 1 from secrets.randbelow arg
        rand_results = [ val - 1 for val in expected_values]
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import get_roll_result
            m.side_effect = rand_results
            output = get_roll_result(4 * [dice_type])
        self.assertEqual(output, 20)

    def test_get_roll_result_multiple_modifier(self):
        dice_type = 10
        expected_values = [2, 4, 6, 8]
        modifier = 7
        # function should add one to random value
        # so remove 1 from secrets.randbelow arg
        rand_results = [ val - 1 for val in expected_values]
        with mock.patch('secrets.randbelow') as m:
            from crypt_roll.utils import get_roll_result
            m.side_effect = rand_results
            output = get_roll_result(4 * [dice_type], modifier)
        self.assertEqual(output, 27)
