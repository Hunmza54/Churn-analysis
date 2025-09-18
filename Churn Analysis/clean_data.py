import pandas as pd
df = pd.read_csv("telco-customer-churn.csv")

print(df.shape)      # rows and columns
print(df.info())     # datatypes and nulls


# Convert TotalCharges to numeric (force errors to NaN)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Check missing values
print(df.isnull().sum())

df["TotalCharges"].fillna(0, inplace=True)

print(df.isnull().sum())


df["SeniorCitizen"] = df["SeniorCitizen"].map({1: "Yes", 0: "No"})

# Strip whitespace
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Check unique values
for col in df.select_dtypes(include="object").columns:
    print(col, df[col].unique())

# Replace "No internet service" with "No"
cols = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", 
        "TechSupport", "StreamingTV", "StreamingMovies"]

for col in cols:
    df[col] = df[col].replace({"No internet service": "No"})

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

print("After transforming")

# Save cleaned data (no index column)
df.to_csv("/Users/Hamza/Desktop/Telco-Customer-Churn-Clean.csv", index=False)

