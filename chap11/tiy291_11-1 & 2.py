import unittest
from chap11.city_functions import city_country

class cityCountryTest(unittest.TestCase ):
    """Testing city_country function"""

    def test_city_country(self):
        area = city_country("centurion", "south africa")
        self.assertEqual(area, "Centurion, South Africa")

    def test_city_country_population(self):
        testAll = city_country("santiago", "chile", population=1000)
        self.assertEqual(testAll, "Santiago, Chile - population 1000")

    def test_city_country_population2(self):
        testAll2 = city_country("santiago", "chile", 1000)
        self.assertEqual(testAll2, "Santiago, Chile - population 1000")

if __name__ == "__main__":
    unittest.main()


