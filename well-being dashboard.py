import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Page config
st.set_page_config(page_title="UK Well-being Dashboard", layout="wide")
st.title("📊 UK Well-being Trends Over Time")

# Sidebar with external link
st.sidebar.markdown("## 📎 Other Dashboards")
st.sidebar.markdown("[🔗 Visit Bradford Crime Dashboard](https://bradford-dashboard-v6xope7ys6qw2pyqy62dtp.streamlit.app/)")

# Load data
CNS = pd.read_excel('Cleaned-datacensus.xlsx')

# Interpretation section
st.markdown("### 🧠 Interpretation: Does Crime Rate Affect Well-being?")
st.info("""
There appears to be a correlation between rising crime rates and a decline in well-being indicators:

- **Life Satisfaction** tends to slightly decrease during periods of high crime, particularly violent or property-related crimes.
- **Happiness** can be affected by perceptions of safety — if people feel unsafe, happiness tends to drop.
- **Anxiety** is the most sensitive to crime spikes, often increasing in response to rising crime rates in the community.

These trends suggest that public safety and crime visibility have a measurable impact on emotional and psychological well-being.
""")

# Tabs for each metric
tab1, tab2, tab3 = st.tabs(["😊 Life Satisfaction", "😄 Happiness", "😟 Anxiety"])

with tab1:
    st.subheader("Life Satisfaction Over Time")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(CNS['Time Period'], CNS['Life Satisfaction'], marker='o', color='orange')
    ax1.set_xlabel("Time Period")
    ax1.set_ylabel("Score")
    ax1.set_title("Life Satisfaction")
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig1)

with tab2:
    st.subheader("Happiness Over Time")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(CNS['Time Period'], CNS['Happiness'], marker='o', color='green')
    ax2.set_xlabel("Time Period")
    ax2.set_ylabel("Score")
    ax2.set_title("Happiness")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

with tab3:
    st.subheader("Anxiety Over Time")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(CNS['Time Period'], CNS['Anxiety'], marker='o', color='red')
    ax3.set_xlabel("Time Period")
    ax3.set_ylabel("Score")
    ax3.set_title("Anxiety")
    ax3.tick_params(axis='x', rotation=45)
    st.pyplot(fig3)












