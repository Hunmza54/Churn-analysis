# ===============================
# 1. Import Libraries
# ===============================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set style
sns.set(style="whitegrid")

# ===============================
# 2. Load Cleaned Data
# ===============================
df = pd.read_csv("clean_data.csv")

# Quick look
print(df.shape)
print(df.info())
df.head()


print("Churn Counts:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

# ===============================
# 4. Churn Distribution
# ===============================
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)
plt.title("Overall Churn Distribution")
plt.show()

# ===============================
# 5. Churn by Contract Type
# ===============================
plt.figure(figsize=(8,5))
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Churn by Contract Type")
plt.show()

# ===============================
# 6. Churn by Tenure (Customer Lifetime)
# ===============================
plt.figure(figsize=(8,5))
sns.histplot(df, x="tenure", hue="Churn", multiple="stack", bins=30)
plt.title("Churn by Tenure")
plt.show()

# ===============================
# 7. Churn by Monthly Charges
# ===============================
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

# ===============================
# 8. Churn by Internet Service
# ===============================
plt.figure(figsize=(8,5))
sns.countplot(x="InternetService", hue="Churn", data=df)
plt.title("Churn by Internet Service Type")
plt.show()

# ===============================
# 9. Correlation Heatmap (Numeric Features)
# ===============================
plt.figure(figsize=(10,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
