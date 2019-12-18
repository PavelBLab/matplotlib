import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# from matplotlib import style
# style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv('dataset.csv')
# print(dataset)
print(dataset.columns)

start_date = '2005-01-01'
end_date = '2005-12-31'
leap_day = '-02-29'
scatter_year = 2015

# print(date)
# print(high_record)
# print(np.max(high_record))

# highest_temperature = list()
# lowest_temperature = list()
temperature = list()
for year in range(2005, 2015):
    # print(year)
    # print(type(str(year)))
    # print(str(year) + start_date[4:], str(year) + end_date[4:])
    high_record = dataset[dataset['Element'] == 'TMAX'][dataset['Date'] >= str(year) + start_date[4:]][dataset['Date'] <= str(year) + end_date[4:]][dataset['Date'] != str(year) + leap_day]['Data_Value']
    low_record = dataset[dataset['Element'] == 'TMIN'][dataset['Date'] >= str(year) + start_date[4:]][dataset['Date'] <= str(year) + end_date[4:]][dataset['Date'] != str(year) + leap_day]['Data_Value']

    # highest_temperature.append((str(year), np.max(high_record)))
    # lowest_temperature.append((str(year), np.min(low_record)))
    temperature.append((str(year), np.max(high_record), np.min(low_record)))

# print(highest_temperature, lowest_temperature)
# print(temperature)

# df_highest = pd.DataFrame(highest_temperature, columns=['Date', 'Maximum temperature'])
# df_lowest = pd.DataFrame(lowest_temperature, columns=['Date', 'Minimum temperature'])
# df_temperature= pd.merge(pd.DataFrame(highest_temperature, columns=['Date', 'Maximum temperature']), pd.DataFrame(lowest_temperature, columns=['Date', 'Minimum temperature']),  how='outer', left_on='Date', right_on='Date')

df_temperature = pd.DataFrame(temperature, columns=['Date', 'Maximum temperature', 'Minimum temperature'])
# print(df_temperature)

#### df_temperature = pd.DataFrame({'Date': date,
####                    'Maximum temperature': high_record,
####                    'Minimum temperature': low_record})
#### df.set_index('Date', inplace=True)
#### print(df)

scatter_list = list()
df_scatter = dataset[dataset['Element'] == 'TMAX'][dataset['Date'] >= str(scatter_year) + start_date[4:]][dataset['Date'] <= str(scatter_year) + end_date[4:]][dataset['Date'] != str(scatter_year) + leap_day][['Date', 'Data_Value']]
# print(df_scatter)
# print(len(df_scatter))


sns.set()
plt.figure(figsize=(10, 5))
plt.ylim((np.min(df_temperature['Minimum temperature']) - 150, np.max(df_temperature['Maximum temperature']) + 150))
#### plt.plot(high_record, 'r-', low_record, 'b-') #r & b are colors
#### plt.axes(frameon=False)
plt.plot(df_temperature['Maximum temperature'],
         '-',
         marker='.',
         markerfacecolor='darkred',
         markersize=10,
         color='darkred',
         linewidth=2)
plt.plot(df_temperature['Minimum temperature'],
         '--',
         marker='.',
         markerfacecolor='darkblue',
         markersize=10,
         color='darkblue',
         linewidth=2)
# print(df_temperature['Maximum temperature'].tolist())

text_high = df_temperature['Maximum temperature'].tolist()
text_low = df_temperature['Minimum temperature'].tolist()
x_coords = range(len(df_temperature['Maximum temperature']))
y_coords_max = df_temperature['Maximum temperature'].tolist()
y_coords_min = df_temperature['Minimum temperature'].tolist()

# for i in enumerate(text_high):
#     print(i)

for index, value in enumerate(text_high): # enumerate create a turple
    x = x_coords[index]
    y = y_coords_max[index]
    plt.scatter(x, y, marker='.', color='darkred')
    plt.text(x-0.1, y+30, str(value)+'°C', fontsize=10)

for index, value in enumerate(text_low):
    x = x_coords[index]
    y = y_coords_min[index]
    plt.scatter(x, y, marker='.', color='darkblue')
    plt.text(x-0.2, y-50, str(value)+'°C', fontsize=10)


plt.title('Temperature evolution in Amsterdam, North Holland, Netherlands', color='grey')
plt.legend(['Maximum temperature (tenths of degrees C)', 'Minimum temperature (tenths of degrees C)'], loc='lower right', frameon = True, shadow = True)
# plt.xticks([year for year in range(2005, 2015)])
plt.xticks([index for index in range(0, len(temperature))], [year for year in range(2005, 2015)]) # plt.xticks(indexes, values)

# print(df['Minimum temperature'])
# print(len(df_temperature['Maximum temperature']))
# print(range(len(df_temperature['Maximum temperature'])))
plt.fill_between(range(len(df_temperature['Maximum temperature'])),
                 df_temperature['Maximum temperature'],
                 df_temperature['Minimum temperature'],
                 color='orange',
                 alpha = 0.1)



# plt.scatter('2007',100)
# plt.scatter(1,100)

# sns.despine(right=True, top=True, offset=20)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off')
# plt.box(False) #delete frame

plt.show()