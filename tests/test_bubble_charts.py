import unittest
import pandas as pd
from scripts.bubble_charts import BubbleCharts

class TestBubbleCharts(unittest.TestCase):

    def setUp(self):
        # Sample data to test the BubbleCharts class
        data = {
            'X': [1, 2, 3, 4, 5],
            'Y': [10, 20, 25, 30, 35],
            'Size': [100, 200, 300, 400, 500]
        }
        self.df = pd.DataFrame(data)
        self.bubble_charts = BubbleCharts(self.df)

    def test_plot_bubble_chart(self):
        # This test checks if the plot_bubble_chart method runs without errors
        try:
            self.bubble_charts.plot_bubble_chart('X', 'Y', 'Size')
        except Exception as e:
            self.fail(f"plot_bubble_chart raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
