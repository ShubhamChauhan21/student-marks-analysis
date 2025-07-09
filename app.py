
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit page settings
st.set_page_config(page_title="Student EDA Dashboard", layout="wide")
st.title("📊 Student Marks EDA & Statistics Dashboard")

# Sidebar info
st.sidebar.title("📌 Project Info")
st.sidebar.markdown("**Submitted by:** Shubham Chauhan")
st.sidebar.markdown("**Topic:** EDA & Descriptive Statistics Tool")
st.sidebar.markdown("**College:** [DTSS college of Commerce]")
st.sidebar.markdown("Guidence:[Prof.Rahul Jadhav]")

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    st.subheader("🔍 Dataset Overview")
    st.write(f"✅ Rows: {df.shape[0]}  |  ✅ Columns: {df.shape[1]}")
    st.write("📌 Column Data Types:")
    st.write(df.dtypes)

    st.subheader("🚫 Missing Values")
    st.write(df.isnull().sum())

    st.subheader("📈 Descriptive Statistics")
    st.write(df.describe())

    st.subheader("📊 Central Tendency")
    st.write("▶️ Mean:")
    st.write(df.mean(numeric_only=True))
    st.write("▶️ Median:")
    st.write(df.median(numeric_only=True))
    st.write("▶️ Mode:")
    st.write(df.mode(numeric_only=True).iloc[0])
    st.write("▶️ Standard Deviation:")
    st.write(df.std(numeric_only=True))

    st.subheader("📉 Distribution Plots")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

    st.subheader("📌 Correlation Heatmap")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)

    if "Grade" in df.columns:
        st.subheader("🎓 Grade Distribution")
        grade_counts = df["Grade"].value_counts()
        fig3, ax3 = plt.subplots()
        ax3.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=90)
        ax3.set_title("Grade Distribution")
        st.pyplot(fig3)

else:
    st.info("⬆️ Please upload a CSV file to begin analysis")
