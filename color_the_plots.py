import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame({'x': range(1, 11),
                   'y1': np.random.randn(10),
                   'y2': np.random.randn(10) + range(1, 11),
                   'y3': np.random.randn(10) + range(11, 21)})
print(df)

# multiple line plot
plt.plot('x',
         'y1',
         data=df,
         marker='o',
         markerfacecolor='#1B75BC',
         markersize=12,
         color='skyblue',
         linewidth=4)
plt.plot('x',
         'y2',
         data=df,
         marker='',
         color='olive',
         linewidth=2,
         label="something")
plt.plot('x',
         'y3',
         data=df,
         marker='',
         color='olive',
         linewidth=2,
         linestyle='dashed',
         label="toto")
plt.legend()
plt.show()
