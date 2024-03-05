import unittest

from RouletteSimulator.bet import (
    BlackBet,
    RedBet,
    ColumnBet,
    DozenBet,
    LowBet,
    HighBet,
    OneNumberBet,
    TwoNumbersBet,
    ThreeNumbersBet,
    FourNumbersBet,
    SixNumbersBet,
    EvenBet,
    OddBet
)

class TestColorBet(unittest.TestCase):
    RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

    def test_positive_red(self):
        red_bet = RedBet()
        for num in self.RED_NUMBERS:
            num = str(num)
            self.assertTrue(red_bet.check_number(num))

    def test_positive_black(self):
        black_bet = BlackBet()
        for num in self.BLACK_NUMBERS:
            num = str(num)
            self.assertTrue(black_bet.check_number(num))

    def test_negative_red(self):
        red_bet = RedBet()
        for num in self.BLACK_NUMBERS:
            num = str(num)
            self.assertFalse(red_bet.check_number(num))
        self.assertFalse(red_bet.check_number('0'))
        self.assertFalse(red_bet.check_number('00'))

    def test_negative_black(self):
        black_bet = BlackBet()
        for num in self.RED_NUMBERS:
            num = str(num)
            self.assertFalse(black_bet.check_number(num))
        self.assertFalse(black_bet.check_number('0'))
        self.assertFalse(black_bet.check_number('00'))

class TestThreeToOneBet(unittest.TestCase):
    def test_positive_dozen(self):
        for num in range(1, 12):
            self.assertTrue(DozenBet(1).check_number(num))
        for num in range(13, 24):
            self.assertTrue(DozenBet(2).check_number(num))
        for num in range(25, 36):
            self.assertTrue(DozenBet(3).check_number(num))

    def test_positive_column(self):
        for num in range(1, 37):
            column_id = num % 3
            if column_id == 0: column_id += 3
            self.assertTrue(ColumnBet(column_id).check_number(num))   

    def test_negative_dozen(self):
        for num in range(1, 12):
            self.assertFalse(DozenBet(2).check_number(num))
            self.assertFalse(DozenBet(3).check_number(num))
        for num in range(13, 24):
            self.assertFalse(DozenBet(1).check_number(num))
            self.assertFalse(DozenBet(3).check_number(num))
        for num in range(25, 36):
            self.assertFalse(DozenBet(1).check_number(num))
            self.assertFalse(DozenBet(2).check_number(num))

        for i in range(1, 4):
            self.assertFalse(DozenBet(i).check_number('0'))
            self.assertFalse(DozenBet(i).check_number('00'))

    def test_negative_column(self):
        for num in range(1, 37):
            column_id = num % 3
            if column_id == 0: column_id += 3
            for i in range(1, 4):
                if i == column_id:
                    continue
                self.assertFalse(ColumnBet(i).check_number(num))

        for i in range(1, 4):
            self.assertFalse(ColumnBet(i).check_number('0'))
            self.assertFalse(ColumnBet(i).check_number('00'))

class TestParityBet(unittest.TestCase):
    def test_positive_odd(self):
        odd_bet = OddBet()
        for num in range(1, 37, 2):
            num = str(num)
            self.assertTrue(odd_bet.check_number(num))

    def test_positive_even(self):
        even_bet = EvenBet()
        for num in range(2, 37, 2):
            num = str(num)
            self.assertTrue(even_bet.check_number(num))

    def test_negative_odd(self):
        odd_bet = OddBet()
        for num in range(2, 37, 2):
            self.assertFalse(odd_bet.check_number(num))
        self.assertFalse(odd_bet.check_number('0'))
        self.assertFalse(odd_bet.check_number('00'))

    def test_negative_even(self):
        even_bet = EvenBet()
        for num in range(1, 37, 2):
            self.assertFalse(even_bet.check_number(num))
        self.assertFalse(even_bet.check_number('0'))
        self.assertFalse(even_bet.check_number('00'))

class TestHalfBet(unittest.TestCase):
    def test_positive_low(self):
        low_bet = LowBet()
        for num in range(1, 19):
            num = str(num)
            self.assertTrue(low_bet.check_number(num))

    def test_positive_high(self):
        high_bet = HighBet()
        for num in range(19, 37):
            num = str(num)
            self.assertTrue(high_bet.check_number(num))

    def test_negative_low(self):
        low_bet = LowBet()
        for num in range(19, 37):
            self.assertFalse(low_bet.check_number(num))
        self.assertFalse(low_bet.check_number('0'))
        self.assertFalse(low_bet.check_number('00'))

    def test_negative_high(self):
        high_bet = HighBet()
        for num in range(1, 19):
            self.assertFalse(high_bet.check_number(num))
        self.assertFalse(high_bet.check_number('0'))
        self.assertFalse(high_bet.check_number('00'))

class TestNumberBet(unittest.TestCase):
    def test_single_positive(self):
        for num in range(1, 37):
            num = str(num)
            self.assertTrue(OneNumberBet([num]).check_number(num))

        self.assertTrue(OneNumberBet(['0']).check_number('0'))
        self.assertTrue(OneNumberBet(['00']).check_number('00'))

    def test_single_negative(self):
        with self.assertRaises(Exception):
            _ = OneNumberBet(['1', '2'])

        for num in range(1, 37):
            for num2 in range(1, 37):
                if num2 == num:
                    continue

                self.assertFalse(OneNumberBet([str(num2)]).check_number(str(num)))
                self.assertFalse(OneNumberBet([str(num)]).check_number(str(num2)))
                self.assertFalse(OneNumberBet(['0']).check_number(str(num2)))
                self.assertFalse(OneNumberBet(['00']).check_number(str(num2)))
                self.assertFalse(OneNumberBet(['0']).check_number(str(num)))
                self.assertFalse(OneNumberBet(['00']).check_number(str(num)))

        self.assertFalse(OneNumberBet(['0']).check_number('00'))
        self.assertFalse(OneNumberBet(['00']).check_number('0'))

    def test_two_positive(self):
        for row in range(12):
            triplets = list(map(str, [3 * row + i for i in range(1, 4)]))
            for i in range(2):
                num1, num2 = triplets[i], triplets[i + 1]
                self.assertTrue(TwoNumbersBet([num1, num2]).check_number(num1))
                self.assertTrue(TwoNumbersBet([num1, num2]).check_number(num2))
                self.assertTrue(TwoNumbersBet([num2, num1]).check_number(num1))
                self.assertTrue(TwoNumbersBet([num2, num1]).check_number(num2))

            if row != 0:
                for num in triplets:
                    number_below = str(int(num) - 3)
                    self.assertTrue(TwoNumbersBet([num, number_below]).check_number(num))
                    self.assertTrue(TwoNumbersBet([num, number_below]).check_number(number_below))
                    self.assertTrue(TwoNumbersBet([number_below, num]).check_number(number_below))
                    self.assertTrue(TwoNumbersBet([number_below, num]).check_number(num))

            if row != 11:
                for num in triplets:
                    number_below = str(int(num) + 3)
                    self.assertTrue(TwoNumbersBet([num, number_below]).check_number(num))
                    self.assertTrue(TwoNumbersBet([num, number_below]).check_number(number_below))
                    self.assertTrue(TwoNumbersBet([number_below, num]).check_number(number_below))
                    self.assertTrue(TwoNumbersBet([number_below, num]).check_number(num))

    def test_two_negative(self):
        with self.assertRaises(Exception):
            _ = TwoNumbersBet(['1', '2', '3'])
        with self.assertRaises(Exception):
            _ = TwoNumbersBet(['1'])
        
        for i in range(37):
            for j in [2, 4, 5] + [i for i in range(7, 37)]:
                with self.assertRaises(Exception):
                    _ = TwoNumbersBet([str(i), str(i + j)])

            with self.assertRaises(Exception):
                _ = TwoNumbersBet([str(i), '0'])

            with self.assertRaises(Exception):
                _ = TwoNumbersBet([str(i), '00'])

    def test_three_positive(self):
        for row in range(12):
            triplets = list(map(str, [3 * row + i for i in range(1, 4)]))
            bet = ThreeNumbersBet(triplets)
            for num in triplets:
                self.assertTrue(bet.check_number(num))

    def test_three_negative(self):
        with self.assertRaises(Exception):
            _ = ThreeNumbersBet(['1', '2'])
        with self.assertRaises(Exception):
            _ = ThreeNumbersBet(['1'])
        with self.assertRaises(Exception):
            _ = ThreeNumbersBet(['1', '2', '3', '4'])
        
        # Check illegal triplets
        for i in range(37):
            with self.assertRaises(Exception):
                _ = ThreeNumbersBet([str(i), str(i + 1), str(i + 3)])
            with self.assertRaises(Exception):
                _ = ThreeNumbersBet([str(i), str(i + 2), str(i + 3)])
            with self.assertRaises(Exception):
                _ = ThreeNumbersBet([str(i), str(i + 2), str(i + 4)])
            with self.assertRaises(Exception):
                _ = ThreeNumbersBet([str(i), str(i + 3), str(i + 6)])
            with self.assertRaises(Exception):
                _ = ThreeNumbersBet([str(i), str(i + 1), '0'])
            with self.assertRaises(Exception):
                _ = ThreeNumbersBet([str(i), str(i + 1), '00'])

    def test_four_positive(self):
        for row in range(12):
            triplets = list(map(str, [3 * row + i for i in range(1, 4)]))
            for i in range(2):
                num1, num2 = triplets[i], triplets[i + 1]
            if row != 0:
                num3, num4 = str(int(num1) - 3), str(int(num2) - 3)
                numbers = [num1, num2, num3, num4]
                bet = FourNumbersBet(numbers)
                for num in numbers:
                    self.assertTrue(bet.check_number(num))
            if row != 11:
                num3, num4 = str(int(num1) + 3), str(int(num2) + 3)
                numbers = [num1, num2, num3, num4]
                bet = FourNumbersBet(numbers)
                for num in numbers:
                    self.assertTrue(bet.check_number(num))

    def test_four_negative(self):
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['1', '2', '3'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['1', '2'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['1'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['1', '2', '3', '4', '5'])

        # Check several illegal quartets
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['1', '2', '3', '4'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['1', '2', '5', '6'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['1', '2', '7', '8'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['0', '1', '2', '3'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['00', '1', '2', '3'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['-1', '0', '1', '2'])
        with self.assertRaises(Exception):
            _ = FourNumbersBet(['34', '35', '37', '38'])

    def test_six_positive(self):
        for row in range(0, 12, 2):
            triplets1 = list(map(str, [3 * row + i for i in range(1, 4)]))
            triplets2 = list(map(str, [3 * row + i + 3 for i in range(1, 4)]))
            numbers = triplets1 + triplets2
            bet = SixNumbersBet(numbers)
            for num in numbers:
                self.assertTrue(bet.check_number(num))

    def test_six_negative(self):
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['1', '2', '3', '4', '5'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['1', '2', '3', '4'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['1', '2', '3'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['1', '2'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['1'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['1', '2', '3', '4', '5', '6', '7'])
        
        # Check several illegal sextets
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['1', '2', '3', '4', '5', '7'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['0', '1', '2', '3', '4', '5'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['-1', '0', '1', '2', '3', '4'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['00', '1', '2', '3', '4', '5'])
        with self.assertRaises(Exception):
            _ = SixNumbersBet(['32', '33', '34', '35', '36', '37'])

if __name__ == '__main__':
    unittest.main()
