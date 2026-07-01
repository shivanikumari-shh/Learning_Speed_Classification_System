# 📊 Learning Speed Classification System

A Data Science & Machine Learning project that automatically classifies students into **Fast**, **Moderate**, and **Slow** learners based on their academic performance and engagement using **K-Means Clustering**.

---

## 🎯 Problem Statement
In large classrooms, it is difficult for teachers to track every student's learning pace individually. This system analyzes student performance data and automatically groups them by learning speed — helping educators give personalized attention where it's needed most.

---

## 🛠️ Technologies Used
| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas & NumPy | Data processing & feature engineering |
| Scikit-learn | K-Means Clustering & evaluation metrics |
| Matplotlib & Seaborn | Data visualization |
| Streamlit | Interactive web dashboard |
| Jupyter Notebook | Step-by-step analysis |

---

## 📁 Project Structure
---

## ⚙️ How to Run

### 1️⃣ Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### 2️⃣ Run Jupyter Notebook
Open `LEARNING_SPEED_PROJECT.ipynb` and run all cells step by step

### 3️⃣ Launch Dashboard
```bash
streamlit run dashboard.py
```

---

## 🔄 Project Pipeline
| Step | Description |
|------|-------------|
| 📥 Data Collection | Synthetic dataset of 300 students with academic & engagement features |
| 🧹 Data Cleaning | Handled missing values using median imputation |
| ⚙️ Feature Engineering | Created `average_score`, `engagement_index`, `learning_consistency` |
| 📏 Scaling | Applied StandardScaler to normalize all features |
| 🤖 Clustering | K-Means algorithm with 3 clusters |
| 🏷️ Labeling | Clusters mapped to Fast / Moderate / Slow learner categories |
| 📊 Evaluation | Silhouette Score & Davies-Bouldin Index |
| 🖥️ Dashboard | Interactive Streamlit app with filters & visualizations |

---

## 📊 Results
- 🟢 **Fast Learners** — ~105 students (high scores + high engagement)
- 🟡 **Moderate Learners** — ~104 students (average performance)
- 🔴 **Slow Learners** — ~91 students (need extra attention)

---

## 👩‍💻 Author
**Shivani Kumari**
- GitHub: [@shivanikumari-shh](https://github.com/shivanikumari-shh)
