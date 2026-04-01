# iris-visuals
The visualizations helped reveal clear patterns in both datasets. For the Iris dataset, it was easy to see that petal length and width are strong indicators of species, especially since Setosa appears completely separated from the other two species. Versicolor and Virginica overlap slightly, but still show noticeable differences in their petal measurements. This suggests that petal-related features are the most useful for classification.

For the loan dataset, the graphs showed that most loans fall within a certain range, with fewer extreme values. The loan status chart highlights how many loans are fully paid versus defaulted, which gives insight into overall risk. Additionally, the scatterplot between interest rate and loan amount suggests that higher loans may sometimes come with higher interest rates, indicating a relationship between risk and loan size. Overall, the visualizations made it easier to identify trends that wouldn’t be obvious just by looking at raw data.
README

Project Title: Data Visualization Analysis of Iris and Loan Datasets

Purpose:
The purpose of this project is to explore and analyze two datasets using data visualization techniques. The Iris dataset is used to examine differences between species based on physical characteristics, while the loan dataset is analyzed to uncover patterns and trends related to financial data.

Class Design & Implementation:
This project uses Python with libraries including pandas, matplotlib, seaborn, and scikit-learn. The program is structured into two main parts:
1. Iris Dataset Analysis
2. Loan Dataset Analysis

Data is loaded into pandas DataFrames and visualizations are generated using matplotlib and seaborn.

Attributes:
- Iris dataset features: sepal length, sepal width, petal length, petal width, species
- Loan dataset features: loan amount, interest rate, loan status (and others depending on dataset)

Methods:
- Scatter plots to compare relationships between variables
- Box plots to show distributions and differences between groups
- Histograms to show frequency distributions
- Count plots to show categorical breakdowns
- Pair plots to visualize relationships across all variables

Limitations:
- The loan dataset may require cleaning depending on missing or inconsistent data
- Visualizations are limited to selected features and may not capture all relationships
- No predictive modeling was performed, only exploratory analysis

Conclusion:
The project demonstrates how visualization can reveal patterns and insights in datasets. The Iris dataset shows clear separability between species, while the loan dataset highlights trends in loan distribution and risk factors.
