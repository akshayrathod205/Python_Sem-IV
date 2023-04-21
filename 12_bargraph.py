import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Great Britain', 'Russia', 'Germany', 'Japan']
gold_medals = [57, 48, 39, 25, 20, 10]
silver_medals = [28, 30, 21, 25, 18, 16]

# Plotting the bar graph
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35  # width of the bars
ind = range(len(countries))

# Adjusting x-axis positions for silver bars
silver_ind = [x + width for x in ind]

gold_bars = ax.bar(ind, gold_medals, width, label='Gold Medals')
silver_bars = ax.bar(silver_ind, silver_medals, width, label='Silver Medals')  # Adjusting x-axis positions

# Adding labels and title
ax.set_xlabel('Countries')
ax.set_ylabel('Medal Count')
ax.set_title('Gold and Silver Medals by Country')
ax.set_xticks([i + width/2 for i in ind])  # Centering x-ticks
ax.set_xticklabels(countries)
ax.legend()

plt.show()
