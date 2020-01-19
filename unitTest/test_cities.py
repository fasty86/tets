import unittest
from city_finctions import get_location


class LocationTestCase(unittest.TestCase):
    """" Tets for location  """

    def test_city_country(self):
        location = get_location('moscow', 'russia')
        self.assertEqual(location, 'Moscow, Russia')

    def test_city_country_population(self):
        location =  get_location('tallin', 'lithuania', '760000')
        self.assertEqual(location, 'Tallin, Lithuania - population 750000')

if __name__ == '__main__':
    unittest.main()
