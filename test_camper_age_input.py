import unittest
from Main import camper_age_input

class MyTestCase(unittest.TestCase):
    def test_multi(self):
        self.assertEquals(camper_age_input.convert_to_months(5, 6), 30)

if __name__ == '__main__':
    unittest.main()
