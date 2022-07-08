from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(15,7))

scale = "log"
# scale = "linear"

big_cores, big_ls, big_mg, big_cl, big_f, big_oh, big_sum = load_from_file_long("big.csv", "\t", 1)
medium_cores, medium_ls, medium_mg, medium_cl, medium_f, medium_oh, medium_sum = load_from_file_long("medium.csv", "\t", 1)
small_cores, small_ls, small_mg, small_cl, small_f, small_oh, small_sum = load_from_file_long("small.csv", "\t", 1)

def plot_compare(title, axis, big_vec, medium_vec, small_vec):
    plot_fig(axis, big_cores, big_vec, 's', 'blue', 'Big model', 1.0, 'black', 5)
    plot_fig(axis, medium_cores, medium_vec, 'o', 'red', 'Medium model', 1.0, 'black', 5)
    plot_fig(axis, small_cores, small_vec, 'D', 'green', 'Small model', 1.0, 'black', 5)
    axis.set_title(title)

plot_compare("Mg equation", ax[0][0], big_mg, medium_mg, small_mg)
plot_compare("Film equation", ax[0][1], big_f, medium_f, small_f)
plot_compare("Cl equation", ax[0][2], big_cl, medium_cl, small_cl)
plot_compare("OH equation", ax[1][0], big_oh, medium_oh, small_oh)
plot_compare("Level set equation", ax[1][1], big_ls, medium_ls, small_ls)
plot_compare("Total", ax[1][2], big_sum, medium_sum, small_sum)

for axes in ax.flat:
    # axes.set_ylim(0, 80)
    # axes.set_xlim(0, 50)
    axes.set_ylabel("Wall time (s)")
    axes.set_xlabel("Number of cores")
    # # axes.yaxis.set_major_locator(MultipleLocator(50))
    # # axes.yaxis.set_minor_locator(MultipleLocator(50))
    # axes.legend(loc="upper right")
    axes.set_yscale(scale)

handles, labels = ax[0][0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3)

plt.tight_layout()
fig.subplots_adjust(bottom=0.14)
plt.savefig(f'scaling_ind_{scale}.png', dpi=300)
plt.show()
