import pandas as pd

df=pd.read_csv("data/customer_churn.csv")
df["TotalCharges"]=pd.to_numeric(df["TotalCharges"], errors="coerce")
if df["TotalCharges"].isnull().sum(0)>0:
    df["TotalCharges"]=df["TotalCharges"].fillna(df["TotalCharges"].median())
for col in df.select_dtypes(include="object").columns:
    df[col]=df[col].fillna(df[col].mode()[0])
print("Shape:",df.shape)
print("\n missing values")
print(df.isnull().sum())
print("\nDuplicate rows:",df.duplicated().sum())

if df.duplicated().sum()>0:
     df=df.drop_duplicates()
     print("\Shape after romoving duplicates:",df.shape)

print("\nChurn Distribution")
print(df["Churn"].value_counts())

df.to_csv("data/customer_churn_cleaned.csv",index=False)

print("\nCleaned dataset saved successfully.")