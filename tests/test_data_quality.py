# tests/test_data_quality.py

import unittest
import pandas as pd
from scripts.data_quality import DataQualityCheck

class TestDataQualityCheck(unittest.TestCase):
    def setUp(self):
        # Sample DataFrame for testing
        self.df = pd.DataFrame({
            'Column1': [1, 2, 3, -1],
            'Column2': [4, -5, 6, -7]
        })
        self.quality_check = DataQualityCheck(self.df)

    def test_check_missing_values(self):
        # Test for missing values
        result_missing_values = self.quality_check.check_missing_values()
        expected_missing_values = pd.Series([0, 0], index=['Column1', 'Column2'])
        pd.testing.assert_series_equal(result_missing_values, expected_missing_values)

    def test_check_negative_values(self):
        # Test for negative values
        result_negative_values = self.quality_check.check_negative_values(['Column1', 'Column2'])
        # Correct the expected result based on the sample DataFrame
        expected_negative_values = pd.Series([1, 2], index=['Column1', 'Column2'])
        pd.testing.assert_series_equal(result_negative_values, expected_negative_values)

    def test_plot_outliers(self):
        # Example test for plot_outliers method
        # Note: You might need to mock the plotting methods or check for plot creation if needed
        self.quality_check.plot_outliers(['Column1', 'Column2'])
        # Add assertions if you want to verify plot behavior

if __name__ == '__main__':
    unittest.main()
