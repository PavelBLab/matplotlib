import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.text(0.5, 0.8, 'Test', color='red',
        bbox=dict(facecolor='none', edgecolor='red'))

ax.text(0.5, 0.6, 'Test', color='blue',
        bbox=dict(facecolor='none', edgecolor='blue', pad=20.0))

ax.text(0.5, 0.4, 'Test', color='green',
        bbox=dict(facecolor='none', edgecolor='green', boxstyle='round'))

ax.text(0.5, 0.2, 'Test', color='black',
        bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))


#
# ax.text((bars_list[0].get_x() + bars_list[end_cost_element].get_x())/2 * 1.1,
#         (bars_list[0].get_height() + bars_list[end_cost_element].get_height())/2 * y_max_scale,
#         f"{deviation:.1f}%",
#         ha='center',
#         color='white',
#         size=10,
#         fontsize=12,
#         fontweight="bold",
#         family=font_family,
#         bbox=dict(facecolor=red_or_green(deviation),
#                   edgecolor='white',
#                   boxstyle='round,pad=1,rounding_size=1.7',
#                   # boxstyle='circle,pad=0.2',
#                   ))



plt.show()