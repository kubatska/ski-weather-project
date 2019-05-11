from SkiWeather import *
import unittest


class TestSkiWeather(unittest.TestCase):
    # module for testing SkiWeather class
    def setUp(self):
        self.instance = data()

    def test_name(self):
        self.assertEqual(self.instance.name(), 'Podobovets and Pilipets')

    def test_date(self):
        self.assertEqual(self.instance.date(), ['2019-05-14'])

    def test_totalSnowfall_cm(self):
        self.assertEqual(self.instance.totalSnowfall_cm(), [0])

    def test_chanceofsnow(self):
        self.assertEqual(self.instance.chanceofsnow(), [0])

    def test_chanceoffog(self):
        self.assertEqual(self.instance.chanceoffog(), [0, 0, 0, 0])

    def test_chanceofthunder(self):
        self.assertEqual(self.instance.chanceofthunder(), [0, 0, 0, 0])

    def test_chanceofwindy(self):
        self.assertEqual(self.instance.chanceofwindy(), [0, 0, 0, 0])

    def test_snowfall_cm(self):
        self.assertEqual(self.instance.snowfall_cm(), [0, 0, 0, 0])

    def test_visibility(self):
        self.assertEqual(self.instance.visibility(), [10, 10, 10, 0])

    def test_bottom_min(self):
        self.assertEqual(self.instance.bottom_min(), [11])

    def test_bottom_max(self):
        self.assertEqual(self.instance.bottom_max(), [7])

    def test_mid_min(self):
        self.assertEqual(self.instance.mid_min(), [9])

    def test_mid_max(self):
        self.assertEqual(self.instance.mid_max(), [8])

    def test_top_min(self):
        self.assertEqual(self.instance.top_min(), [7])

    def test_top_max(self):
        self.assertEqual(self.instance.top_max(), [7])

    def test_str(self):
        self.assertEqual(self.instance.__str__(), "Podobovets and Pilipets")

    def test_whether(self):
        self.assertEqual(self.instance.whether(), [False, False, False])

    

def data():
    f = open('check.json', encoding = 'utf-8')
    all_data = json.load(f)
    ski_list = list(key for key in all_data['resorts'])
    resorts_list = Array(len(ski_list))
    for i in range(len(ski_list)):
        resorts_list[i] = SkiWeather(ski_list[i])
    return resorts_list[0]


unittest.main()

