import unittest
import workshop


class TestWorkshop(unittest.TestCase):
    def test_fit(self):
        self.assertEqual(workshop.fit("crapola"), 5)
