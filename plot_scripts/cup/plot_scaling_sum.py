from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))

# scale = "log"
scale = "linear"

big_cores, big_ls, big_mg, big_cl, big_f, big_oh, big_sum = load_from_file_long("big.csv", "\t", 1)
medium_cores, medium_ls, medium_mg, medium_cl, medium_f, medium_oh, medium_sum = load_from_file_long("medium.csv", "\t", 1)
small_cores, small_ls, small_mg, small_cl, small_f, small_oh, small_sum = load_from_file_long("small.csv", "\t", 1)

plot_fig(ax, big_cores, big_sum, 's', 'blue', 'Big model', 1.0, 'black', 5)
plot_fig(ax, medium_cores, medium_sum, 'o', 'red', 'Medium model', 1.0, 'black', 5)
plot_fig(ax, small_cores, small_sum, 'D', 'green', 'Small model', 1.0, 'black', 5)
ax.set_title("Strong scaling")

# ax.set_ylim(0, 80)
# ax.set_xlim(0, 50)
ax.set_ylabel("Wall time (s)")
ax.set_xlabel("Number of cores")
# # axes.yaxis.set_major_locator(MultipleLocator(50))
# # axes.yaxis.set_minor_locator(MultipleLocator(50))
ax.legend(loc="upper right")
ax.set_yscale(scale)

plt.tight_layout()
plt.savefig(f'scaling_sum_{scale}.png', dpi=300)
plt.show()
