#!/usr/bin/env python
# coding: utf-8

#Read the sheet of xls file that has relevant data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('../data/Portfolio_by_delinquency.xls', sheet_name="FedManagedPortbyDelinquencyStat")


#Cleaning the data
delin_df = df.drop(df.index[-21:])
delin_df = delin_df.iloc[5:]
delin_df = delin_df.ffill()


#Extracting numbers of borrowers in dataframe
delin_borrowers_df = delin_df.drop(delin_df.columns[[1, 2, 4, 6, 8, 10, 12]], axis=1)
delin_borrowers_df.columns = ['Year', 'Current Repayment', '31-90 days delinquent', '91-180 days delinquent', '181-270 days delinquent', '271-360 days delinquent', 'Default']

#Using groupby to group the data and get mean for each year
delin_borrowers_df = delin_borrowers_df.groupby(['Year']).mean()
delin_borrowers_df.astype('float').round(1)

#Copying the data into another dataframe for plotting
delin_borrowers_df_plot = delin_borrowers_df.copy()
delin_borrowers_df.reset_index(inplace=True)


#Reshaping the data to use for creating line plot
delin_melted_borrow_df = pd.melt(delin_borrowers_df, id_vars=["Year"], value_vars=delin_borrowers_df.columns[1:], var_name="Status", value_name="Value")


plt.figure(figsize=(10, 6))

# Create line plot
sns.barplot(delin_melted_borrow_df, x="Status", y="Value", hue="Year")  # Transpose the DataFrame for proper x-axis labeling

# Add title and axis labels
plt.title("Delinquency status vs Number of Borrowers")
plt.xlabel("Delinquency status")
plt.ylabel("Borrowers(in million)")

# Rotate x-axis labels (optional)
plt.xticks(rotation=45, fontsize=8)

# Display the plot
plt.show()




