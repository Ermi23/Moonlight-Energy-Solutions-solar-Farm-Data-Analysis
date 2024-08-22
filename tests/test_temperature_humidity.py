import unittest
import pandas as pd
from scripts.temperature_humidity import TemperatureHumidityAnalysis

class TestTemperatureHumidityAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data to test the TemperatureHumidityAnalysis class
        data = {
            'RH': [10, 20, 30, 40, 50],
            'TModA': [15, 25, 35, 45, 55],
            'TModB': [10, 22, 32, 42, 52]
        }
        self.df = pd.DataFrame(data)
        self.temperature_humidity_analysis = TemperatureHumidityAnalysis(self.df)

    def test_plot_temperature_vs_humidity(self):
        try:
            self.temperature_humidity_analysis.plot_temperature_vs_humidity()
        except Exception as e:
            self.fail(f"plot_temperature_vs_humidity raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
