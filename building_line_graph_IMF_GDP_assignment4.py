import os
# print(os.listdir())
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.cm as cm

style.use('ggplot')
import numpy as np
import warnings
warnings.filterwarnings('ignore')

'===================================== IMF source ====================================='
IMF_df = pd.read_csv('WEO_Data.csv')
# print(GDP.head())
# print(IMF_df.columns)
IMF_df.set_index(['Subject Descriptor', 'Units'], inplace=True)
# print(IMF_df.head())
# print(IMF_df.index)
# print(IMF_df.iloc[:3, :3])
# print(IMF_df.columns)

# print(IMF_df.index.is_lexsorted())
# IMF_df.sort_index(inplace=True)
# print(IMF_df.index.is_lexsorted())

# IMF_df = IMF_df.MultiIndex.is_lexsorted()
GDP = IMF_df.loc['Gross domestic product, constant prices', 'Percent change']
# print(GDP)
# print(GDP.columns)
# print([year for year in GDP.columns if len(year) == 4])

filter_column = [year for year in GDP.columns if len(year) == 4]
# print(filter_column)
filter_column.insert(0, GDP.columns[0])
# print(filter_column)
# print(GDP[filter_column].reset_index(drop=True).dropna())

GDP_by_country = GDP[filter_column].reset_index(drop=True).dropna().set_index('Country').T
# print(GDP_by_country.head())
# print(GDP_by_country.dtypes)
'to make your plot work you need to convert the columns that have numbers into numeric'
GDP_by_country = GDP_by_country.apply(pd.to_numeric, errors="ignore")
# print(GDP_by_country.dtypes)

GDP_Europe = GDP_by_country[['Austria',
                             'Belgium',
                             'Bulgaria',
                             'Cyprus',
                             'Denmark',
                             'Finland',
                             'France',
                             'Germany',
                             'Greece',
                             'Hungary',
                             'Ireland',
                             'Italy',
                             'Luxembourg',
                             'Norway',
                             'Spain',
                             'Sweden',
                             'Switzerland',
                             'United Kingdom',
                             ]]
# print(GDP_Europe)
GDP_Netherlands = GDP_by_country['Netherlands']
# print(GDP_Netherlands)

'===================================== Wiki source ====================================='

Netherlands = pd.read_html('https://en.wikipedia.org/wiki/Economy_of_the_Netherlands')
# print(Netherlands)
# print(len(Netherlands))

' Find a dataframe'
# for i in range(len(Netherlands)):
#     print(i)
#     print(Netherlands[i])
#     print('='.center(30,'='))
' This is a dataframe'
# print(Netherlands[5])

' Find a column'
# for i in Netherlands[5]:
    # print(i)
    # print(Netherlands[5][i])
    # print(Netherlands[5]['GDP growth(real)'])
# print(us_states[0]['Abbr']['Abbr'])
GDP_Netherlands_Wiki = Netherlands[5][['Year','GDP growth(real)']].set_index('Year').dropna()
# print(GDP_Netherlands)


'================================== Build a line graph =================================='
fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

'Below 4 lines color all lines with unique color'
number_of_plots = len(GDP_Europe.columns)
colormap = plt.cm.tab20 # colormaps https://matplotlib.org/examples/color/colormaps_reference.html
# print(colormap(0.2))
colors = [colormap(i) for i in np.linspace(0, 1, number_of_plots)]
# print(colors)
# print(np.linspace(0, 1, number_of_plots))
ax1.set_prop_cycle('color', colors)


GDP_Europe.plot(ax = ax1)
GDP_Netherlands.plot(ax=ax1, color='k',linewidth=5)
plt.ylabel('Percent change')
plt.xlabel('Years')
# print(ax1.get_children())
ax1.xaxis.set_label_coords(0.5, -0.08)
plt.xticks(list(range(len(filter_column[1:])))[::3], filter_column[1:][::3])
# print(list(range(len(filter_column[1:])))[::3])
plt.title('Real gross domestic product in the Netherlands vs. Europe',  fontsize=10)
plt.tight_layout(rect=[0.1, 1, 1, 0.9]) # Usually tight_layout() does a pretty good job at positioning everything in good locations so that they don't overlap
plt.legend(loc='upper center', bbox_to_anchor=(0.95, 1.01),
          ncol=3, fontsize=7, fancybox=True, shadow=True)

fig.set_size_inches((15, 7), forward=False) # Adjust size of the picture
fig.savefig('Real gross domestic product in the Netherlands vs. Europe.png', dpi = 600)

plt.show()



