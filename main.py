import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("amazon.csv")

# Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# ---------------- GRAPH 1 ----------------
top_categories = df["category"].value_counts().head(5)

ax[0,0].bar(
    ["Cables", "Watches", "Phones", "TV", "Headphones"],
    top_categories.values
)

ax[0,0].set_title("Top Categories")
ax[0,0].set_xlabel("Category")
ax[0,0].set_ylabel("Count")
ax[0,0].grid(True)

# ---------------- GRAPH 2 ----------------
top_ratings = df["rating"].value_counts().head(5)

ax[0,1].pie(
    top_ratings.values,
    labels=top_ratings.index,
    autopct="%1.1f%%"
)

ax[0,1].set_title("Ratings Distribution")

# ---------------- GRAPH 3 ----------------
ax[1,0].plot(
    top_ratings.index,
    top_ratings.values,
    marker="o"
)

ax[1,0].set_title("Ratings Trend")
ax[1,0].set_xlabel("Rating")
ax[1,0].set_ylabel("Count")
ax[1,0].grid(True)

# ---------------- GRAPH 4 ----------------
ax[1,1].bar(
    top_ratings.index,
    top_ratings.values
)

ax[1,1].set_title("Ratings Count")
ax[1,1].set_xlabel("Rating")
ax[1,1].set_ylabel("Frequency")
ax[1,1].grid(True)

plt.suptitle("Amazon Sales Analys Dashboard")
# Space adjustment
plt.tight_layout()

# Show dashboard
plt.show()