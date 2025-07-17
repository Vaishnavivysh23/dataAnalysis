import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def edaPage():
    st.title("Step-by-Step Data Analysis")

    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.success("✅ File Uploaded Successfully")

        st.header("1. Dataset Overview")
        st.write(f"Shape: {data.shape}")
        st.write(f"Columns: {data.columns.tolist()}")
        st.dataframe(data.head())

        st.header("2. Missing Values")
        st.write(data.isnull().sum())

        st.header("3. Descriptive Statistics")
        st.dataframe(data.describe(include="all"))

        st.header("4. Data Types")
        num_col = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        cat_col = data.select_dtypes(include=['object']).columns.tolist()
        st.write("Numerical Columns:", num_col)
        st.write("Categorical Columns:", cat_col)

        st.header("5. Univariate Analysis")
        col = st.selectbox("Select a column to analyze", data.columns)
        if col in num_col:
            fig = plt.figure()
            sns.histplot(data[col].dropna(), kde=True)
            st.pyplot(fig)
        else:
            fig = plt.figure()
            data[col].value_counts().plot(kind='bar')
            plt.title(f"Value Counts of {col}")
            st.pyplot(fig)

        st.header("6. Box Plot (Outlier Detection)")
        if num_col:
            col2 = st.selectbox("Select numerical column for box plot", num_col)
            fig = plt.figure()
            sns.boxplot(data[col2])
            st.pyplot(fig)

        st.header("7. Correlation Matrix")
        if num_col:
            corr = data[num_col].corr()
            fig = plt.figure(figsize=(10, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm')
            st.pyplot(fig)
edaPage()