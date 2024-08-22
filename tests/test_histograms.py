import unittest
import pandas as pd
from scripts.histograms import Histograms

class TestHistograms(unittest.TestCase):

    def setUp(self):
        # Sample data to test the Histograms class
        data = {
            'Column1': [1, 2, 3, 4, 5],
            'Column2': [5, 4, 3, 2, 1]
        }
        self.df = pd.DataFrame(data)
        self.histograms = Histograms(self.df)

    def test_plot_histograms(self):
        try:
            self.histograms.plot_histograms(['Column1', 'Column2'])
        except Exception as e:
            self.fail(f"plot_histograms raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
