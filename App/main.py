import streamlit as st
import pandas as pd
import sys
import os

# Add your scripts folder to the Python path
# sys.path.append('C:/Moonlight-Energy-Solutions-solar-farm-data-Analysis/scripts')
# Determine the base directory of the project dynamically
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the 'scripts' directory to sys.path
scripts_path = os.path.join(base_dir, 'scripts')
sys.path.append(scripts_path)

from time_series import TimeSeriesAnalysis
from bubble_charts import BubbleCharts
from correlation_analysis import CorrelationAnalysis
from histograms import Histograms
from temperature_humidity import TemperatureHumidityAnalysis
from wind_analysis import WindAnalysis
from z_score import ZScoreAnalysis
# from ..scripts.wind_analysis import WindAnalysis

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

            if len(available_bubble_columns) >= 3:
                x_col = st.selectbox("Select X-axis column", available_bubble_columns, index=0)
                y_col = st.selectbox("Select Y-axis column", available_bubble_columns, index=1)
                size_col = st.selectbox("Select Size column", available_bubble_columns, index=2)
                
                st.write(f"Bubble chart with selected columns: {x_col}, {y_col}, {size_col}")
                bc = BubbleCharts(df)
                bc.plot_bubble_chart_streamlit(x_col, y_col, size_col)
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
                corr_analysis.plot_correlation_matrix_streamlit(corr_columns)

                st.write("Pair Plot:")
                corr_analysis.plot_pairplot_streamlit(corr_columns)
            else:
                st.warning("Please select at least one column for correlation analysis.")
                
                        # Impact of Relative Humidity on Temperature
            st.header("Impact of Relative Humidity on Temperature")
            default_th_columns = ['TModB', 'TModB']
            available_th_columns = [col for col in default_th_columns if col in df.columns]

            ts_columns = st.multiselect(
                "Select columns to plot (Impact of Relative Humidity on Temperature)", df.columns.tolist(), default=available_th_columns
            )

            # Correct the method call
            if ts_columns:
                tsa = TemperatureHumidityAnalysis(df)
                tsa.plot_temperature_vs_humidity_stramlite()  # No argument passed here
            else:
                st.warning("Please select at least one column to plot.")
                
            #     # Wind Speed and Direction Distribution
            # st.header("Wind Speed and Direction Distribution")

            # # List of default columns (modify as needed)
            # default_th_columns = ['WD', 'WS']
            # available_th_columns = [col for col in default_th_columns if col in df.columns]

            # # Select columns for plotting
            # ts_columns = st.multiselect(
            #     "Select columns to plot (Wind Speed and Direction Distribution)", df.columns.tolist(), default=available_th_columns
            # )

            # # Ensure the correct method is called if columns are selected
            # if ts_columns:
            #     tsa = WindAnalysis(df)
            #     tsa.plot_wind_rose_streamlite()
            # else:
            #     st.warning("Please select at least one column to plot.")
            
                        # # Histogram Analysis
            # st.header("Histogram Analysis")

            # # Set default columns to show in the histogram
            # default_hist_columns = ['GHI', 'DNI', 'DHI', 'Tamb']
            # available_hist_columns = [col for col in default_hist_columns if col in df.columns]

            # # Select columns for histogram
            # hist_columns = st.multiselect(
            #     "Select columns to plot histograms", df.columns.tolist(), default=available_hist_columns
            # )

            # if hist_columns:
            #     da = Histograms(df)
            #     da.plot_histograms_streamlite(hist_columns)
            # else:
            #     st.warning("Please select at least one column to plot.")

            # # Z-score Analysis
            # st.header("Z-score Analysis")
            # default_z_score_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'RH', 'WS', 'WSgust', 'WSstdev', 'WD', 'WDstdev', 'BP', 'Precipitation', 'TModA', 'TModB']
            # available_z_score_columns = [col for col in default_z_score_columns if col in df.columns]

            # selected_z_score_columns = st.multiselect(
            #     "Select columns for Z-score analysis", df.columns.tolist(), default=available_z_score_columns
            # )

            # if selected_z_score_columns:
            #     z_score_analysis = ZScoreAnalysis(df)
            #     z_score_analysis.calculate_z_scores(selected_z_score_columns)
            #     z_score_analysis.plot_z_scores_streamlit()
            # else:
            #     st.warning("Please select at least one column for Z-score analysis.")
            
            

if __name__ == "__main__":
    main()
