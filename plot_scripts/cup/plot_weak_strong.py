from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

big_cores, big_ls, big_mg, big_cl, big_f, big_oh, big_sum = load_from_file_long("big.csv", "\t", 1)
medium_cores, medium_ls, medium_mg, medium_cl, medium_f, medium_oh, medium_sum = load_from_file_long("medium.csv", "\t", 1)
small_cores, small_ls, small_mg, small_cl, small_f, small_oh, small_sum = load_from_file_long("small.csv", "\t", 1)
weak_cores, weak_sum, _ = load_from_file("weak.csv", ",", 1)

plot_fig(ax[0], big_cores, big_sum, 's', 'blue', 'Big model', 1.0, 'black', 5)
plot_fig(ax[0], medium_cores, medium_sum, 'o', 'red', 'Medium model', 1.0, 'black', 5)
plot_fig(ax[0], small_cores, small_sum, 'D', 'green', 'Small model', 1.0, 'black', 5)
ax[0].set_title("Strong scaling")

plot_fig(ax[1], weak_cores, weak_sum, 'o', 'orange', '', 1.0, 'black', 5)
ax[1].set_title("Weak scaling")

for i, axes in enumerate(ax.flat):
    axes.set_ylabel("Wall time (s)")
    axes.set_xlabel("Number of cores")
    if i == 0:
        axes.set_yscale("log")
        axes.legend(loc="upper right")
    else:
        axes.set_ylim(0, 40)
        # axes.set_xlim(0, 50)

plt.tight_layout()
plt.savefig(f'weak_strong.png', dpi=300)
plt.show()
