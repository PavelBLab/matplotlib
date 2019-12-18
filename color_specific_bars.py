import matplotlib.pyplot as plt
import numpy as np

'Remove warnings'
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
# TODO: change the bar colors to be less bright blue
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
print(list(bars))
# TODO: make one bar, the python bar, a contrasting color
print(bars[0])
bars[0].set_color('green')



# TODO: soften all labels by turning grey
plt.xticks(pos, languages)
plt.ylabel('% Popularity', color = 'gray')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', color = 'gray')

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.show()