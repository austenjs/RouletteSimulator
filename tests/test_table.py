import unittest

from RouletteSimulator import AmericanTable, EuropeanTable

class TestExistenceOfAllNumbers(unittest.TestCase):
    def test(self):
        table1 = AmericanTable()
        table2 = EuropeanTable()

        for table, expected_num in ((table1, 38), (table2, 37)):
            seen = set()
            for _ in range(1000):
                seen.add(table.roll())
            self.assertTrue(expected_num == len(seen))
