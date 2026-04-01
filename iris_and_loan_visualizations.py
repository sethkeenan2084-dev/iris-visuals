import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Fisher's Iris Dataset Visualizations
# ----------------------------

# Load the Iris dataset
sepal_df = pd.read_csv("Sepal_Data.csv")
petal_df = pd.read_csv("Petal_Data.csv")

# Combine the datasets
combined_df = pd.merge(
    sepal_df,
    petal_df,
    on=["sample_id", "species"]
)

# Scatter Plot: Petal Length vs. Petal Width
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=combined_df,
    x="petal_length",
    y="petal_width",
    hue="species",
    palette="viridis"
)
plt.title("Petal Length vs. Petal Width by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend(title="Species")
plt.savefig("iris_scatter_plot.png")
plt.show()

# Box Plot: Sepal Length by Species
plt.figure(figsize=(8, 6))
sns.boxplot(
    data=combined_df,
    x="species",
    y="sepal_length",
    palette="Set2"
)
plt.title("Distribution of Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.savefig("iris_box_plot.png")
plt.show()

# Pair Plot: Pairwise Relationships
sns.pairplot(
    combined_df,
    vars=["petal_length", "petal_width", "sepal_length", "sepal_width"],
    hue="species",
    palette="husl"
)
plt.savefig("iris_pair_plot.png")
plt.show()

# ----------------------------
# Loan Dataset Visualizations
# ----------------------------

# Load the Loan dataset
loan_df = pd.read_csv("LoanDataset - LoansDatasest.csv")

# Clean and preprocess the data
loan_df["loan_amnt"] = loan_df["loan_amnt"].replace({"£": "", ",": ""}, regex=True).astype(float)
loan_df["loan_int_rate"] = loan_df["loan_int_rate"].fillna(0)

# Bar Plot: Loan Intent vs. Average Loan Amount
plt.figure(figsize=(8, 6))
sns.barplot(
    data=loan_df,
    x="loan_intent",
    y="loan_amnt",
    hue="loan_grade",
    palette="coolwarm"
)
plt.title("Average Loan Amount by Loan Intent and Grade")
plt.xlabel("Loan Intent")
plt.ylabel("Average Loan Amount (£)")
plt.legend(title="Loan Grade")
plt.savefig("loan_bar_plot.png")
plt.show()

# Box Plot: Interest Rates by Loan Grade
plt.figure(figsize=(8, 6))
sns.boxplot(
    data=loan_df,
    x="loan_grade",
    y="loan_int_rate",
    palette="muted"
)
plt.title("Distribution of Interest Rates by Loan Grade")
plt.xlabel("Loan Grade")
plt.ylabel("Interest Rate (%)")
plt.savefig("loan_box_plot.png")
plt.show()

# Scatter Plot: Customer Income vs. Loan Amount
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=loan_df,
    x="customer_income",
    y="loan_amnt",
    hue="Current_loan_status",
    palette="Set1"
)
plt.title("Customer Income vs. Loan Amount by Loan Status")
plt.xlabel("Customer Income (£)")
plt.ylabel("Loan Amount (£)")
plt.legend(title="Loan Status")
plt.savefig("loan_scatter_plot.png")
plt.show()