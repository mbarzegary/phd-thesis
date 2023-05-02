from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))

small_cores, small_eff, medium_cores, medium_eff, big_cores, big_eff, _ = load_from_file_long("efficiency.csv", ",", 1)

plot_fig(ax, small_cores, small_eff, 's', 'blue', 'Big model', 1.0, 'black', 5)
plot_fig(ax, medium_cores, medium_eff, 'o', 'red', 'Medium model', 1.0, 'black', 5)
plot_fig(ax, big_cores, big_eff, 'D', 'green', 'Small model', 1.0, 'black', 5)
ax.set_title("Parallel efficiency")

# ax.set_ylim(0, 80)
# ax.set_xlim(0, 50)
# ax.set_ylabel("Parallel efficiency")
ax.set_xlabel("Number of cores")
# # axes.yaxis.set_major_locator(MultipleLocator(50))
# # axes.yaxis.set_minor_locator(MultipleLocator(50))
ax.legend(loc="upper right")
# ax.set_yscale(scale)

plt.tight_layout()
plt.savefig(f'efficiency.png', dpi=300)
plt.show()
