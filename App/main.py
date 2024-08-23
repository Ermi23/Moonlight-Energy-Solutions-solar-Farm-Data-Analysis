import streamlit as st
import pandas as pd
import sys
import os

# Add your scripts folder to the Python path
sys.path.append('C:/Moonlight-Energy-Solutions-solar-farm-data-Analysis/scripts')

from time_series import TimeSeriesAnalysis
from bubble_charts import BubbleCharts
from correlation_analysis import CorrelationAnalysis

# Function to load the data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def main():
    st.title('Solar Farm Data Analysis')

    # Dropdown to select file
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    selected_file = st.selectbox("Select a file to analyze", files)

    # Load the selected file
    if selected_file:
        file_path = os.path.join(data_dir, selected_file)
        df = load_data(file_path)

        if df is not None:
            st.write("Preview of the data:")
            st.write(df.head())

            # Time Series Analysis
            st.header("Time Series Analysis")
            default_ts_columns = ['GHI', 'DNI', 'DHI', 'Tamb']
            available_ts_columns = [col for col in default_ts_columns if col in df.columns]

            ts_columns = st.multiselect(
                "Select columns to plot (Time Series)", df.columns.tolist(), default=available_ts_columns
            )

            if ts_columns:
                tsa = TimeSeriesAnalysis(df)
                tsa.plot_time_series_streamlit(ts_columns)
            else:
                st.warning("Please select at least one column to plot.")

            # Bubble Chart Analysis
            st.header("Bubble Chart Analysis")
            default_bubble_columns = ['GHI', 'Tamb', 'WS']
            available_bubble_columns = [col for col in default_bubble_columns if col in df.columns]

            if len(available_bubble_columns) == 3:
                x_col, y_col, size_col = available_bubble_columns
                st.write(f"Bubble chart with default columns: {x_col}, {y_col}, {size_col}")
                bc = BubbleCharts(df)
                bc.plot_bubble_chart(x_col, y_col, size_col)
            else:
                st.error("Not enough default columns to plot a bubble chart. Please ensure the data has 'GHI', 'Tamb', and 'WS' columns.")

            # Correlation Analysis
            st.header("Correlation Analysis")
            default_corr_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS']
            available_corr_columns = [col for col in default_corr_columns if col in df.columns]

            corr_columns = st.multiselect(
                "Select columns for correlation analysis", df.columns.tolist(), default=available_corr_columns
            )

            if corr_columns:
                corr_analysis = CorrelationAnalysis(df)
                st.write("Correlation Matrix Heatmap:")
                corr_analysis.plot_correlation_matrix(corr_columns)

                st.write("Pair Plot:")
                corr_analysis.plot_pairplot(corr_columns)
            else:
                st.warning("Please select at least one column for correlation analysis.")

if __name__ == "__main__":
    main()
