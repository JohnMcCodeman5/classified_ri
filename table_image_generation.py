import pandas as pd
from matplotlib import pyplot as plt

dfb = pd.read_csv('comparison_tables/bests.csv')
columns = ['Dim','brute_force','brute_force_time','greedy','greedy_time','local_search','local_search_time','local_search_perm','local_search_perm_time']
dfb1 = dfb[columns]
dfb2 = dfb.drop(columns[1:], axis=1)


# Adjust the figure size based on the number of columns
fig, ax = plt.subplots(figsize=(10, 4)) 
# Hide axes
ax.axis('off')
# Use pandas plotting.table for better control
table = pd.plotting.table(ax, dfb1, loc='center', colWidths=[0.2]*len(dfb1.columns))
# Adjust font size
table.auto_set_font_size(False)
table.set_fontsize(9)
# Save the plot as an image file (e.g., PNG)
plt.savefig('table_images/best_table1.png', bbox_inches='tight', pad_inches=0.1)


table = pd.plotting.table(ax, dfb2, loc='center', colWidths=[0.2]*len(dfb2.columns))
table.auto_set_font_size(False)
table.set_fontsize(9)
plt.savefig('table_images/best_table2.png', bbox_inches='tight', pad_inches=0.1)


dfa = pd.read_csv('comparison_tables/averages.csv')
dfa1 = dfa[columns]
dfa2 = dfa.drop(columns[1:], axis=1)


table = pd.plotting.table(ax, dfa1, loc='center', colWidths=[0.2]*len(dfa1.columns))
table.auto_set_font_size(False)
table.set_fontsize(9)
plt.savefig('table_images/avg_table1.png', bbox_inches='tight', pad_inches=0.1)


table = pd.plotting.table(ax, dfa2, loc='center', colWidths=[0.2]*len(dfa2.columns))
table.auto_set_font_size(False)
table.set_fontsize(9)
plt.savefig('table_images/avg_table2.png', bbox_inches='tight', pad_inches=0.1)