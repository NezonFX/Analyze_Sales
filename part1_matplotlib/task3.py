import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

sky = patches.Rectangle((0, 0), 10, 10, facecolor='skyblue', alpha=0.5)
ax.add_patch(sky)

sun = patches.Circle((8, 8), radius=0.8, facecolor='yellow', edgecolor='orange')
ax.add_patch(sun)

house1 = patches.Rectangle((1, 1), 2.5, 4, facecolor='lightgray', edgecolor='black')
ax.add_patch(house1)

roof1 = patches.Polygon([[1, 5], [2.25, 6.5], [3.5, 5]], facecolor='brown', edgecolor='black')
ax.add_patch(roof1)

door = patches.Rectangle((2, 1), 0.5, 1.5, facecolor='saddlebrown')
ax.add_patch(door)

window = patches.Rectangle((2.7, 3), 0.6, 0.6, facecolor='cyan', edgecolor='black')
ax.add_patch(window)

house2 = patches.Rectangle((5, 1), 3, 3, facecolor='lightyellow', edgecolor='black')
ax.add_patch(house2)

roof2 = patches.Arc((6.5, 4), width=3, height=2, theta1=0, theta2=180, color='darkred', lw=3)
ax.add_patch(roof2)

tree = patches.Ellipse((4.5, 2), width=1, height=2, facecolor='green')
ax.add_patch(tree)

trunk = patches.Rectangle((4.4, 1), 0.2, 1, facecolor='brown')
ax.add_patch(trunk)

plt.savefig('img/task3.png', bbox_inches='tight')
plt.show()