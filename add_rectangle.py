import matplotlib.pyplot as plt

fig, ax = plt.subplots()

'Rectangle(xy, width, height);   xy = (x, y);   xy: (float, float). The bottom and left rectangle coordinates'
children = plt.gca().get_children()
rectangle_1 = plt.Rectangle((children[0].get_x() + abs(children[0].get_x() * 0.1),    # x: (float). The bottom rectangle coordinates. + abs(children[0].get_x() * 0.1) in case get_x() is negative
                            children[0].get_height() * 0.8),    # y: (float). The left rectangle coordinates
                            children[0].get_width() * 0.9,    # width
                            children[0].get_height() * 0.1,    # height
                            color='white',
                            fill=True)    # fill=False leaves only boarders

ax.add_patch(rectangle_1)