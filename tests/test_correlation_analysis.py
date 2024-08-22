import unittest
import pandas as pd
from scripts.correlation_analysis import CorrelationAnalysis

class TestCorrelationAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data to test the CorrelationAnalysis class
        data = {
            'VarA': [1, 2, 3, 4, 5],
            'VarB': [10, 20, 30, 40, 50],
            'VarC': [5, 3, 6, 8, 2],
            'VarD': [7, 9, 2, 3, 6]
        }
        self.df = pd.DataFrame(data)
        self.correlation_analysis = CorrelationAnalysis(self.df)

    def test_plot_correlation_matrix(self):
        # This test checks if the plot_correlation_matrix method runs without errors
        try:
            self.correlation_analysis.plot_correlation_matrix(['VarA', 'VarB', 'VarC', 'VarD'])
        except Exception as e:
            self.fail(f"plot_correlation_matrix raised an exception: {e}")

    def test_plot_pairplot(self):
        # This test checks if the plot_pairplot method runs without errors
        try:
            self.correlation_analysis.plot_pairplot(['VarA', 'VarB', 'VarC', 'VarD'])
        except Exception as e:
            self.fail(f"plot_pairplot raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
