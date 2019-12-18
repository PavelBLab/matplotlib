# get_ipython().magic('matplotlib notebook')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
print(col.to_rgba('blue'))
import matplotlib.cm as cm


'''
we need to define a seed that makes the random numbers predictable. When the value is reset, the same numbers will appear every time. If we do not assign the seed, NumPy automatically selects a random seed value based on the system's random number generator device or on the clock.
If you want seemingly random numbers, do not set the seed. If you have code that uses random numbers that you want to debug, however, it can be very helpful to set the seed before each run so that the code does the same thing every time you run it.
'''

np.random.seed(12345)
df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])
df = df.T
# print(df)
# print(df.columns)

def length(dataframe):
    list = []
    for i in dataframe.columns:
        list.append(len(dataframe[i]))
    return list
# print(length(df))
# print(range(len(df)))


data = length(df) #[3650, 3650, 3650, 3650]
mean_values = np.mean(df)
standart_deviation = np.std(df)
# print(mean_values)
# print(standart_deviation)
x_position = range(len(df.columns))

'''
Strictly speaking a 95% confidence interval means that if we were to take 100 different samples and compute a 95% confidence interval for each sample, then approximately 95 of the 100 confidence intervals will contain the true mean value (μ).
95% = 1.96

The standard error is the approximate standard deviation of a statistical sample population. The standard error is a statistical term that measures the accuracy with which a sample represents a population. In statistics, a sample mean deviates from the actual mean of a population; this deviation is the standard error. The more data points involved in the calculations of the mean, the smaller the standard error tends to be.  
'''
standart_error = 1.96 * standart_deviation / np.sqrt(data[0]) # data[0] is length of the sample 3650
# print(standart_error)
# print(standart_error.iloc[0])


fig, ax = plt.subplots(figsize=(10, 5))
Y_horizontal_line = 42000


# click_ydata = 0
def onclick(event):
    # global click_ydata
    # print(event.ydata)
    plt.cla()
    color_list = color_function(event.ydata)
    # print(color_list)

    # click_ydata = event.ydata # ydata gives y axis value
    ax.axhline(y=event.ydata,
               linewidth=1,
               color='blue',
               zorder=2)

    ax.bar(x_position,
           mean_values,
           yerr=standart_error,
           align='center',
           # alpha=0.5,
           color=color.to_rgba(color_list),
           # color = ['pink'],
           # ecolor='black',
           # capsize=10,
           zorder=1) # order put at the background the figure

    plt.xticks(x_position, df.columns)
    plt.ylabel('number of votes')
    plt.xlabel('Years')
    plt.title('Mean number of votes in a district, marked with 95% confidence Interval')

def color_function(yline):
    color_list = []
    for i in range(len(mean_values)):
        # print(mean_values.iloc[i])
        # print(standart_error.iloc[i])
        low_point = mean_values.iloc[i] - standart_error.iloc[i]
        high_point = mean_values.iloc[i] + standart_error.iloc[i]

        find_color = (high_point - yline)/(high_point - low_point)
        # print(find_color)
        if find_color > 1:
            find_color = 1
        elif find_color < 0:
            find_color = 0
        color_list.append(find_color)
    return color_list
color_list = color_function(Y_horizontal_line)
print(color_list)

#Setup the colormap
# colormap = col.LinearSegmentedColormap.from_list('colormap',['blue', 'gray', 'red'])
# print(cm.cmap_d.keys()) # Use colormaps_reference.py to choose color set
color = cm.ScalarMappable(cmap=cm.cmap_d['Paired']) # The ScalarMappable makes use of data normalization before returning RGBA colors from the given colormap.
color.set_array([])
# Add the colorbar
'-> boundaries=np.linspace(0,2,13)) 0 is starting point, 2 is ending, 13 is number of color sections on color bar, in this case there are 12 sections'
c = plt.colorbar(color, orientation='horizontal', boundaries=np.linspace(0, 1, 11))
c.ax.set_xticklabels(['0%','20%','40%','60%', '80%', '100%'])


# Updating the plot
'''
- x_position is the array with the count of the number of bars.
- mean_values is our array which contains the means or heights of the bars.
- yerr=standart_error sets the heights of the error bars and the standard deviations.
    keyword arguments (yerr=standart_error, align='center', alpha=0.5, color=['red', 'purple', 'yellow', 'black'], ecolor='black', capsize=10, zorder = 2) styles the plot.
- alpha=0.5 makes bars transparent
- zorder put at the background line or bars
'''
ax.bar(x_position,
       mean_values,
       yerr=standart_error,
       align='center',
       #alpha=0.5,
       color=color.to_rgba(color_list),
       # color = ['pink'],
       # ecolor='black',
       # capsize=10,
       zorder = 1)

ax.axhline(y=Y_horizontal_line,
           linewidth=1,
           color='red',
           zorder=2)

plt.xticks(x_position, df.columns)
plt.ylabel('number of votes')
plt.xlabel('Years')
plt.title('Mean number of votes in a district, marked with 95% confidence Interval')
plt.tight_layout(rect=[0.05, 0.05, 0.9, 0.9]) # Usually tight_layout() does a pretty good job at positioning everything in good locations so that they don't overlap


# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)


#Below 2 lines to make graph image full screm
# mng = plt.get_current_fig_manager()
# mng.full_screen_toggle()

# Below is save picture. dpi is size of the picture
# plt.savefig('bar_plot_with_error_bars.png', dpi = 300)

plt.show()
plt.close()


