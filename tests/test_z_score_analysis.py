import unittest
import pandas as pd
from scripts.z_score import ZScoreAnalysis

class TestZScoreAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data to test the ZScoreAnalysis class
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [2, 3, 4, 5, 6]
        }
        self.df = pd.DataFrame(data)
        self.z_score_analysis = ZScoreAnalysis(self.df)

    def test_calculate_z_scores(self):
        self.z_score_analysis.calculate_z_scores(['A', 'B'])
        self.assertTrue('A' in self.z_score_analysis.df_z_scores.columns)
        self.assertTrue('B' in self.z_score_analysis.df_z_scores.columns)
        self.assertTrue('A_outliers' in self.z_score_analysis.df_z_scores.columns)
        self.assertTrue('B_outliers' in self.z_score_analysis.df_z_scores.columns)

    def test_plot_histograms(self):
        try:
            self.z_score_analysis.calculate_z_scores(['A', 'B'])
            self.z_score_analysis.plot_histograms(['A', 'B'])
        except Exception as e:
            self.fail(f"plot_histograms raised an exception: {e}")

    def test_plot_boxplots(self):
        try:
            self.z_score_analysis.calculate_z_scores(['A', 'B'])
            self.z_score_analysis.plot_boxplots(['A', 'B'])
        except Exception as e:
            self.fail(f"plot_boxplots raised an exception: {e}")

    def test_plot_scatter(self):
        try:
            self.z_score_analysis.calculate_z_scores(['A', 'B'])
            self.z_score_analysis.plot_scatter(['A', 'B'])
        except Exception as e:
            self.fail(f"plot_scatter raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
