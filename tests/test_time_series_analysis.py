import unittest
import pandas as pd
from scripts.time_series import TimeSeriesAnalysis

class TestTimeSeriesAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data to test the TimeSeriesAnalysis class
        data = {
            'Timestamp': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1]
        }
        self.df = pd.DataFrame(data)
        self.time_series_analysis = TimeSeriesAnalysis(self.df)

    def test_plot_time_series(self):
        try:
            self.time_series_analysis.plot_time_series(['A', 'B'])
        except Exception as e:
            self.fail(f"plot_time_series raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
