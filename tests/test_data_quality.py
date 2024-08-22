import unittest
import pandas as pd
from scripts.data_quality import DataQualityCheck

class TestDataQualityCheck(unittest.TestCase):

    def setUp(self):
        # Sample data to test the DataQualityCheck class
        data = {
            'Column1': [1, -2, 3, None, 5],
            'Column2': [10, None, -30, 40, 50]
        }
        self.df = pd.DataFrame(data)
        self.data_quality_check = DataQualityCheck(self.df)

    def test_check_missing_values(self):
        expected_missing_values = pd.Series([1, 1], index=['Column1', 'Column2'])
        result_missing_values = self.data_quality_check.check_missing_values()
        pd.testing.assert_series_equal(result_missing_values, expected_missing_values)

    def test_check_negative_values(self):
        expected_negative_values = pd.Series([1, 2], index=['Column1', 'Column2'])
        result_negative_values = self.data_quality_check.check_negative_values(['Column1', 'Column2'])
        pd.testing.assert_series_equal(result_negative_values, expected_negative_values)

    def test_plot_outliers(self):
        try:
            self.data_quality_check.plot_outliers(['Column1', 'Column2'])
        except Exception as e:
            self.fail(f"plot_outliers raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
