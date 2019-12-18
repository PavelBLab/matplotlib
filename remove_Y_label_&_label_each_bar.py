import matplotlib.pyplot as plt
import numpy as np

'Remove warnings'
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

plt.figure()

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
x_position = np.arange(len(languages))
print(x_position)
popularity = [56, 39, 34, 34, 29]

# change the bar colors to be less bright blue
bars = plt.bar(x_position, popularity, align='center', linewidth=0, color='lightslategrey')
# make one bar, the python bar, a contrasting color
bars[0].set_color('#1F77B4')

# soften all labels by turning grey
# We need the names of the languages to go along our x-axis, one name below each bar.
plt.xticks(x_position, languages, alpha=0.8)

# TODO: remove the Y label since bars are directly labeled
# plt.ylabel('% Popularity', alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# TODO: direct label each bar with Y axis values
for object in plt.gca().get_children():
    print(object)
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, # x
                   bar.get_height() - 4, # y
                   str(int(bar.get_height())) + '%', # text
                   ha='center', color='white', fontsize=11)
plt.show()