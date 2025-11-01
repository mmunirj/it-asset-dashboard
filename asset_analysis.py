import pandas as pd

ad=pd.read_csv('C:/Users/badar/Downloads/asset_inventory.csv')

print(ad.head())


ad.info()
ad.describe(include='all')

ad.isnull().sum()

ad["AssignedTo"].fillna("Unassigned",inplace=True)

ad["PurchaseDate"] = pd.to_datetime(ad["PurchaseDate"])


from datetime import datetime

ad["DeviceAgeDays"] = (datetime.now() - ad["PurchaseDate"]).dt.days
ad["DeviceAgeYears"] = (ad["DeviceAgeDays"] / 365).round(1)

ad["Location"].value_counts()

ad["Model"].value_counts()

ad["Status"].value_counts()

ad.groupby("Location")["DeviceAgeYears"].mean().round(1)


ad[ad["AssignedTo"] != "Unassigned"].shape[0]

ad.sort_values("DeviceAgeYears", ascending=False).head()


import matplotlib.pyplot as plt
import seaborn as sns

plt.Figure(figsize=(8,5))
sns.countplot(x="Location",data=ad, palette="viridis")
plt.title("Devices per Location")
plt.xticks(rotation=30)
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(ad["DeviceAgeYears"], bins=10, kde=True, color="teal")
plt.title("Device Age Distribution (Years)")
plt.show()

status_counts = ad["Status"].value_counts()
plt.pie(status_counts,labels=status_counts.index, autopct="%1.1f%%", startangle=120)
plt.show()