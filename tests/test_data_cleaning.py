import unittest
import pandas as pd
from scripts.data_cleaning import DataCleaning

class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        # Sample data to test the DataCleaning class
        data = {
            'Column1': [1, 2, None, 4, 5],
            'Column2': ['A', 'B', 'C', None, 'E'],
            'Comments': ['Comment1', None, 'Comment3', 'Comment4', None]
        }
        self.df = pd.DataFrame(data)
        self.data_cleaning = DataCleaning(self.df)

    def test_drop_na_comments(self):
        # Expected DataFrame after dropping rows where 'Comments' is NaN
        expected_df = pd.DataFrame({
            'Column1': [1.0, None, 4.0],
            'Column2': ['A', 'C', None],
            'Comments': ['Comment1', 'Comment3', 'Comment4']
        }).reset_index(drop=True)

        # Run the drop_na_comments method
        result_df = self.data_cleaning.drop_na_comments().reset_index(drop=True)

        # Assert the DataFrame equality
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_fill_missing_values(self):
        # Expected DataFrame after filling NaN in 'Column1' with 0
        expected_df = pd.DataFrame({
            'Column1': [1.0, 2.0, 0.0, 4.0, 5.0],
            'Column2': ['A', 'B', 'C', None, 'E'],
            'Comments': ['Comment1', None, 'Comment3', 'Comment4', None]
        })

        # Run the fill_missing_values method
        result_df = self.data_cleaning.fill_missing_values('Column1', 0)

        # Assert the DataFrame equality
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()
