import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Learning Speed Classification", layout="wide")

st.title("📊 Learning Speed Classification System")
st.write("Students classified into Fast, Moderate, and Slow learners using K-Means clustering.")

df = pd.read_csv(r"C:\Users\dell\Downloads\classified_students.csv")

# --- Top metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Fast Learners", (df['learning_speed'] == 'Fast Learner').sum())
col2.metric("Moderate Learners", (df['learning_speed'] == 'Moderate Learner').sum())
col3.metric("Slow Learners", (df['learning_speed'] == 'Slow Learner').sum())

st.divider()

# --- Filter ---
selected = st.multiselect(
    "Filter by learning speed",
    options=df['learning_speed'].unique(),
    default=df['learning_speed'].unique()
)
filtered_df = df[df['learning_speed'].isin(selected)]

# --- Bar Chart ---
st.subheader("Distribution of Learners")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x='learning_speed',
              order=['Fast Learner', 'Moderate Learner', 'Slow Learner'],
              palette={'Fast Learner': '#2ecc71', 'Moderate Learner': '#f1c40f', 'Slow Learner': '#e74c3c'},
              ax=ax1)
ax1.set_xlabel("")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# --- Scatter Plot ---
st.subheader("Average Score vs Engagement Index")
fig2, ax2 = plt.subplots()
sns.scatterplot(
    data=filtered_df, x='engagement_index', y='average_score',
    hue='learning_speed',
    palette={'Fast Learner': '#2ecc71', 'Moderate Learner': '#f1c40f', 'Slow Learner': '#e74c3c'},
    ax=ax2
)
st.pyplot(fig2)

# --- Data Table ---
st.subheader("Student Data")
st.dataframe(filtered_df[['student_id', 'name', 'average_score', 
                           'engagement_index', 'learning_consistency', 'learning_speed']])

# --- Download Button ---
st.download_button(
    "⬇️ Download Classified Data",
    filtered_df.to_csv(index=False),
    file_name="classified_students.csv",
    mime="text/csv"
)