import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm
print(cm.cmap_d.keys())


# Have colormaps separated into categories:
# http://matplotlib.org/examples/color/colormaps_reference.html
cmaps = [('Perceptually Uniform Sequential', [
            'viridis', 'plasma', 'inferno', 'magma']),
         ('Sequential', [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         ('Sequential (2)', [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']),
         ('Diverging', [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ('Miscellaneous', [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]



#Setup the colormap
# colormap = col.LinearSegmentedColormap.from_list('colormap',['blue', 'gray', 'red'])
# color = cm.ScalarMappable(cmap=colormap)
# print(cm.cmap_d.keys()) # Use colormaps_reference.py to choose color set
color = cm.ScalarMappable(cmap=cm.cmap_d['Paired']) # The ScalarMappable makes use of data normalization before returning RGBA colors from the given colormap.
color.set_array([])


# Add the colorbar
'-> boundaries=np.linspace(0,2,13)) 0 is starting point, 2 is ending, 13 is number of color sections on color bar, in this case there are 12 sections'
c = plt.colorbar(color, orientation='horizontal', boundaries=np.linspace(0, 1, 11))

# label color bar x axis
c.ax.set_xticklabels(['0%','20%','40%','60%', '80%', '100%'])