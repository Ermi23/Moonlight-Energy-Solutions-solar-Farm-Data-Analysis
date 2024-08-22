import unittest
import pandas as pd
from scripts.wind_analysis import WindAnalysis

class TestWindAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data to test the WindAnalysis class
        data = {
            'WD': [0, 90, 180, 270, 360],
            'WS': [5, 10, 15, 20, 25]
        }
        self.df = pd.DataFrame(data)
        self.wind_analysis = WindAnalysis(self.df)

    def test_plot_wind_rose(self):
        try:
            self.wind_analysis.plot_wind_rose()
        except Exception as e:
            self.fail(f"plot_wind_rose raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
