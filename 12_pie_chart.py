import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Great Britain', 'Russia', 'Germany', 'Japan']
gold_medals = [57, 48, 39, 25, 20, 10]

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(gold_medals, labels=countries, autopct='%1.1f%%', startangle=90, shadow=True)

# Adding title and legend
ax.set_title('Gold Medals Obtained by Countries in Olympics 2012')
ax.legend(countries, title='Countries', loc='upper right')

plt.show()
