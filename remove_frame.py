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

plt.bar(pos, popularity, align='center')
plt.xticks(pos, languages)
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

# TODO: remove the frame of the chart
plt.box(False)

'OR'
# TODO: remove the frame of the chart
for object in plt.gca().get_children(): # gca = get current axes
    print(object)

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()