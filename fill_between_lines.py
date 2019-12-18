import matplotlib.pyplot as plt
'Remove warnings'
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


plt.fill_between(range(len(df_temperature['Maximum temperature'])),
                 df_temperature['Maximum temperature'],
                 df_temperature['Minimum temperature'],
                 color='orange',
                 alpha = 0.1)