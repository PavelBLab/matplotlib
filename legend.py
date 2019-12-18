import matplotlib.pyplot as plt

'Remove warnings'
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


plt.legend(['Maximum temperature (tenths of degrees C)', 'Minimum temperature (tenths of degrees C)'], loc='lower right', frameon = True, shadow = True)

plt.legend(facecolor='lightblue',
           shadow = 'True',
           loc = 'center', #or loc can be numbers loc=10
           title = 'title for legend')