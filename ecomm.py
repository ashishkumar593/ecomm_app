import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("This is a app for ecomm i am creating")
    st.sidebar.title("you can upload your file here")

    upload_file = st.sidebar.file_uploader("Upload CSV", type=["csv", 'xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file, encoding='utf-8')
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success("file uploaded successfully")

            st.subheader("i am going to show you the data")

            st.subheader("Lets see some more details in data")
            st.write("Shape of the data:", data.shape)
            st.write("Columns in the data:", data.columns.tolist())
            st.write("Missing values in the data:", data.isnull().sum())
            st.write("Statistical summary of the data:", data.describe())
            st.write("Data types of the columns:", data.dtypes)
            st.write("Sample data:", data.sample(5))

            

            st.dataframe(data.head())
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()