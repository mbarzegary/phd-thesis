from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))

disp_0, force_0 = load_from_file("force_displ.csv", ",", 8, 9, 1, 1000)
disp_28, force_28 = load_from_file("force_displ.csv", ",", 6, 7, 1, 1000)
disp_77, force_77 = load_from_file("force_displ.csv", ",", 4, 5, 1, 1000)
disp_124, force_124 = load_from_file("force_displ.csv", ",", 2, 3, 1, 1000)
disp_170, force_170 = load_from_file("force_displ.csv", ",", 0, 1, 1, 1000)

plot_fig(ax, disp_0, force_0, None, 'blue', '0 days', 1.0, 'black', 5)
plot_fig(ax, disp_28, force_28, None, 'red', '28 days', 1.0, 'black', 5)
plot_fig(ax, disp_77, force_77, None, 'green', '77 days', 1.0, 'black', 5)
plot_fig(ax, disp_124, force_124, None, 'purple', '124 days', 1.0, 'black', 5)
plot_fig(ax, disp_170, force_170, None, 'orange', '170 days', 1.0, 'black', 5)
# ax.set_title("Title")

ax.set_ylim(0, 450)
ax.set_xlim(0, 0.14)
ax.set_ylabel("Force (N)")
ax.set_xlabel("Displacement [mm]")
# axes.yaxis.set_major_locator(MultipleLocator(50))
# axes.yaxis.set_minor_locator(MultipleLocator(50))
ax.legend(loc="bottom right")

plt.tight_layout()
plt.savefig('force_displacement.png', dpi=300)
plt.show()
