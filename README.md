# Task 1 - Bank Term Deposit Prediction

**Objective:**  
Predict whether a bank customer will subscribe to a term deposit as a result of a marketing campaign.

**Dataset:**  
Bank Marketing Dataset (`bank.csv`) from UCI Machine Learning Repository.

**Techniques & Models Used:**  
- **Data preprocessing:** Label encoding for categorical variables  
- **Feature scaling:** StandardScaler (for Logistic Regression)  
- **Models:** Logistic Regression, Random Forest  
- **Evaluation Metrics:** Confusion Matrix, F1 Score, Classification Report, ROC Curve  
- **Explainability:** Random Forest feature importance + individual predictions

**Outcome:**  
The models successfully predicted term deposit subscription, and feature importance analysis provided insights into the key factors influencing customer decisions.

**Instructions to Run:**  
1. Clone the repository:  
```bash
git clone https://github.com/YourUsername/DevelopersHub-DS-Internship.git

# Task 02 – Customer Segmentation Using Unsupervised Learning

## 📌 Objective
To segment customers based on their spending behavior and propose data-driven marketing strategies for each identified group.

## 🗂 Dataset
Mall Customers Dataset

## 🔍 Exploratory Data Analysis (EDA)
- Analyzed customer age, annual income, and spending score
- Identified spending patterns and relationships between features

## 🧠 Methodology
- Applied **K-Means Clustering** to group customers
- Used the **Elbow Method** to determine the optimal number of clusters
- Performed **Dimensionality Reduction (PCA / t-SNE)** for cluster visualization

## 📊 Results & Insights
- Customers were successfully segmented into distinct clusters
- Each cluster represents a unique spending behavior and income pattern

## 📈 Marketing Strategy Suggestions
- High income & high spending: Premium offers and loyalty programs  
- High income & low spending: Personalized discounts and engagement campaigns  
- Low income & high spending: Value deals and budget-friendly promotions  
- Low income & low spending: Awareness campaigns and seasonal offers  

## 🛠 Tools & Libraries
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

## 🎯 Skills Gained
- Unsupervised Learning (K-Means)
- Dimensionality Reduction (PCA / t-SNE)
- Customer Segmentation
- Data-driven Strategy Development

