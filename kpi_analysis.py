import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# KPIs
total_revenue = df["Revenue"].sum()
average_revenue = df["Revenue"].mean()
total_orders = df["Orders"].sum()

# Conversion Rate
df["Conversion Rate"] = (df["Orders"] / df["Visitors"]) * 100

# Retention Rate
df["Retention Rate"] = (df["Returning_Customers"] / df["Orders"]) * 100

# KPI Summary
print("========== KPI SUMMARY ==========")
print("Total Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Total Orders:", total_orders)

print("\nConversion & Retention")
print(df[["Month","Conversion Rate","Retention Rate"]])

# Dashboard
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Revenue"], marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.savefig("dashboard.png")
plt.show()
plt.savefig("dashboard.png")
plt.close()