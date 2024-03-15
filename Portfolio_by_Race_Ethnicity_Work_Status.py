# %%
import pandas as pd
import matplotlib.pyplot as mp
df = pd.read_csv('Race-Ethnicity-Education-Loan.csv')

# %% Only take out columns that are relevant
new_df = df[['year', 'Category', 'Education_Installment_Loans']].copy()


# %% Create separate dataframes for each ethnicity for ease of processing
df_white = new_df[(new_df == 'White, non-Hispanic').any(axis=1)]
df_black = new_df[(new_df == 'Black, non-Hispanic').any(axis=1)]
df_hispanic = new_df[(new_df == 'Hispanic').any(axis=1)]
df_other = new_df[(new_df == 'Other').any(axis=1)]

# %% Plot trend lines for all ethnicities on the same graph
ax = df_white.plot(style= '-o', x = 'year', y='Education_Installment_Loans', color="#9C33FF")
df_black.plot(ax = ax, style= '-^', x = 'year', y='Education_Installment_Loans', color="#F633FF")
df_hispanic.plot(ax = ax, style= '-s', x = 'year', y='Education_Installment_Loans', color="#FF336B")
df_other.plot(ax = ax, style= '-*', x = 'year', y='Education_Installment_Loans', color="#FF8633")
ax.legend(["White, non Hispanic", "Black, non Hispanic", "Hispanic", "Other"])
ax.set_ylabel("Amount Borrowed (In thousands)")

# %% Plot a cumulative pie chart by summing up 30 years of data
total_white = df_white['Education_Installment_Loans'].sum()
total_black = df_black['Education_Installment_Loans'].sum()
total_hispanic = df_hispanic['Education_Installment_Loans'].sum()
total_other = df_other['Education_Installment_Loans'].sum()

totals_df = pd.DataFrame({'Category' : ['White, non Hispanic', 'Black, non Hispanic', 'Hispanic', 'Other'], 'Total amount borrowed (1989-2022)' : [total_white, total_black, total_hispanic, total_other]}, index=['White, NH*', 'Black, NH*', 'Hisp', 'Other'])

plot = totals_df.plot.pie(x = '*NH = non hispanic', y='Total amount borrowed (1989-2022)', figsize=(25, 10), autopct='%1.1f%%', colors=["#9C33FF", "#F633FF", "#FF336B", "#FF8633"], textprops={'fontsize': 12})
plot.legend(loc=2, fontsize=13)
plot.text(-1, -1.5, "*NH = Non Hispanic")

# %% Work status analysis
df2 = pd.read_csv('Work-Status-Education_Loan.csv')

# %% Only take out columns that are relevant
new_df2 = df2[['year', 'Category', 'Education_Installment_Loans']].copy()

# %% Create separate dataframes for each work status for ease of processing
df_employee = new_df2[(new_df2 == 'Employee').any(axis=1)]
df_self = new_df2[(new_df2 == 'Self-employed').any(axis=1)]
df_retired = new_df2[(new_df2 == 'Retired').any(axis=1)]
df_unemp = new_df2[(new_df2 == 'Other not working').any(axis=1)]


# %% Plot trend lines for all work statuses on the same graph
ax = df_employee.plot(style= '-o', x = 'year', y='Education_Installment_Loans', color="#33FF80")
df_self.plot(ax = ax, style= '-^', x = 'year', y='Education_Installment_Loans', color="#339FFF")
df_retired.plot(ax = ax, style= '-s', x = 'year', y='Education_Installment_Loans', color="#33FFD7")
df_unemp.plot(ax = ax, style= '-*', x = 'year', y='Education_Installment_Loans', color="#3352FF")
ax.legend(["Employee", "Self-employed", "Retired", "Unemployed"])
ax.set_ylabel("Amount Borrowed (In thousands)")

# %%  Plot a cumulative pie chart by summing up 30 years of data
total_employee = df_employee['Education_Installment_Loans'].sum()
total_self= df_self['Education_Installment_Loans'].sum()
total_retired = df_retired['Education_Installment_Loans'].sum()
total_unemp = df_unemp['Education_Installment_Loans'].sum()


totals_df2 = pd.DataFrame({'Category' : ['Employee', 'Self-employed', 'Retired', 'Unemployed'], 'Total amount borrowed (1989-2022)' : [total_employee, total_self, total_retired, total_unemp]}, index=['Employee', 'Self-Employed', 'Retired', 'Unemployed'])

plot = totals_df2.plot.pie(y='Total amount borrowed (1989-2022)', figsize=(30, 10), autopct='%1.1f%%', textprops={'fontsize': 12}, colors=["#33FF80", "#339FFF", "#33FFD7", "#3352FF"])
plot.legend(fontsize=13)




