import matplotlib.pyplot as plt

'Remove warnings'
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


'https://stackoverflow.com/questions/8248467/matplotlib-tight-layout-doesnt-take-into-account-figure-suptitle'
'https://stackoverflow.com/questions/16150819/common-xlabel-ylabel-for-matplotlib-subplots'


plt.title('Temperature evolution in Amsterdam, North Holland, Netherlands', color='grey')
plt.xlabel('X label')
plt.ylabel('Y label')

plt.suptitle('Understanding Distributions Through Sampling')



'And title for subplots'
import matplotlib.pyplot as plt
fig, ax = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(6, 6))
fig.text(0.5, 0.04, 'common X', ha='center')
fig.text(0.04, 0.5, 'common Y', va='center', rotation='vertical')