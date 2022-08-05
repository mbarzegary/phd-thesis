from helpers import *

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8,4))

case1_run1_time, _, case1_run1_loss = load_from_file_long("case1-run1-deg.txt", "\t", 1)
case1_run2_time, _, case1_run2_loss = load_from_file_long("case1-run2-deg.txt", "\t", 1)
case1_run3_time, _, case1_run3_loss = load_from_file_long("case1-run3-deg.txt", "\t", 1)

case2_run1_time, _, case2_run1_loss = load_from_file_long("case2-run1-deg.txt", "\t", 1)
case2_run2_time, _, case2_run2_loss = load_from_file_long("case2-run2-deg.txt", "\t", 1)
case2_run3_time, _, case2_run3_loss = load_from_file_long("case2-run3-deg.txt", "\t", 1)

plot_fig(ax[0], case1_run1_time, case1_run1_loss, 's', 'blue', 'D = 0.001', 1.0, 'black', 5)
plot_fig(ax[0], case1_run2_time, case1_run2_loss, 'o', 'red', 'D = 0.01', 1.0, 'black', 5)
plot_fig(ax[0], case1_run3_time, case1_run3_loss, 'D', 'green', 'D = 0.05', 1.0, 'black', 5)
ax[0].set_title("Case 1")

plot_fig(ax[1], case2_run1_time, case2_run1_loss, 's', 'blue', 'D = 0.001', 1.0, 'black', 5)
plot_fig(ax[1], case2_run2_time, case2_run2_loss, 'o', 'red', 'D = 0.01', 1.0, 'black', 5)
plot_fig(ax[1], case2_run3_time, case2_run3_loss, 'D', 'green', 'D = 0.05', 1.0, 'black', 5)
ax[1].set_title("Case 2")

#
for i, axes in enumerate(ax.flat):
    axes.set_ylabel("Mass loss (%)")
    axes.set_xlabel("Time (nondimentional)")

handles, labels = ax[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3)

plt.tight_layout()
fig.subplots_adjust(bottom=0.25)
plt.savefig('degradation_rate.png', dpi=300)
plt.show()
