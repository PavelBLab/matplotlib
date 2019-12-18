import matplotlib.pyplot as plt
import numpy as np


plt.figure()
# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# pos = np.arange(len(languages))
# popularity = [56, 39, 34, 34, 29]
#
# # change the bar colors to be less bright blue
# bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
# for spine in plt.gca().spines.values():
#     spine.set_visible(False)


for object in plt.gca().get_children():
    print(object)

print(np.random.rand(5))