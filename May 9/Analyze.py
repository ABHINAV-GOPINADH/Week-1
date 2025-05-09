import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# --- OOP Classes ---
class CSVLoader:
    def __init__(self, file):
        self.file = file
        self.data = None

    def load(self):
        try:
            self.data = pd.read_csv(self.file)
            return self.data
        except Exception as e:
            st.error(f"❌ Error loading file: {e}")
            return None


class DataProcessor:
    def __init__(self, data):
        self.data = data

    def summary_statistics(self):
        return self.data.describe()

    def get_numeric_columns(self):
        return self.data.select_dtypes(include='number').columns.tolist()

    def get_column_average(self, column):
        return self.data[column].mean()


class Plotter:
    def __init__(self, data):
        self.data = data

    def line_plot(self, column):
        fig, ax = plt.subplots()
        ax.plot(self.data[column], marker='o')
        ax.set_title(f"{column} Trend")
        ax.set_xlabel("Index")
        ax.set_ylabel(column)
        ax.grid(True)
        st.pyplot(fig)

    def histogram(self, column):
        fig, ax = plt.subplots()
        ax.hist(self.data[column], bins=10, color='skyblue', edgecolor='black')
        ax.set_title(f"Histogram of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)


# --- Streamlit UI ---
st.title("Analyzer")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    # Step 1: Load CSV
    loader = CSVLoader(uploaded_file)
    df = loader.load()

    if df is not None:
        st.success("✅ Data Loaded Successfully")
        st.write("### Preview of Data", df.head())

        # Step 2: Process
        processor = DataProcessor(df)
        st.write("### Summary Statistics")
        st.write(processor.summary_statistics())

        numeric_columns = processor.get_numeric_columns()
        if numeric_columns:
            selected_column = st.selectbox("Select a column to analyze", numeric_columns)

            avg = processor.get_column_average(selected_column)
            st.info(f"📈 Average of **{selected_column}**: {avg:.2f}")

            # Step 3: Plot
            plotter = Plotter(df)

            st.write("### Line Plot")
            plotter.line_plot(selected_column)

            st.write("### Histogram")
            plotter.histogram(selected_column)
        else:
            st.warning("⚠️ No numeric columns found in the uploaded dataset.")
