import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_csv('sales_data.csv')

# Step 2: Preview
print(df.head())

# Step 3: Create subplots
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 📈 Line Plot: Sales Trend
ax[0, 0].plot(df['Month'], df['Sales'], marker='o', color='blue')
ax[0, 0].set_title("Monthly Sales")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Sales")
ax[0, 0].grid()

# 📊 Bar Chart: Profit
ax[0, 1].bar(df['Month'], df['Profit'], color='green')
ax[0, 1].set_title("Monthly Profit")
ax[0, 1].set_xlabel("Month")
ax[0, 1].set_ylabel("Profit")
ax[0, 1].grid(axis='y')

# 🔴 Scatter Plot: Sales vs Profit
ax[1, 0].scatter(df['Sales'], df['Profit'], color='red', s=100)
ax[1, 0].set_title("Sales vs Profit")
ax[1, 0].set_xlabel("Sales")
ax[1, 0].set_ylabel("Profit")
ax[1, 0].grid()

# 📦 Histogram: Sales Distribution
ax[1, 1].hist(df['Sales'], bins=5, color='orange', edgecolor='black')
ax[1, 1].set_title("Sales Distribution")
ax[1, 1].set_xlabel("Sales")
ax[1, 1].set_ylabel("Frequency")
ax[1, 1].grid(axis='y')

fig.suptitle("Business Growth Trends and Performance Dashboard")
plt.tight_layout()
plt.show()