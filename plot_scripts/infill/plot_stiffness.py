from helpers import *

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8,9))

case1_run1_time, _, case1_run1_loss = load_from_file_long("case1-run1-deg.txt", "\t", 1)
_, case1_run1_compliance = load_from_file("case1-run1-obj.txt", "\t", 0)
case1_run2_time, _, case1_run2_loss = load_from_file_long("case1-run2-deg.txt", "\t", 1)
_, case1_run2_compliance = load_from_file("case1-run2-obj.txt", "\t", 0)
case1_run3_time, _, case1_run3_loss = load_from_file_long("case1-run3-deg.txt", "\t", 1)
_, case1_run3_compliance = load_from_file("case1-run3-obj.txt", "\t", 0)

case2_run1_time, _, case2_run1_loss = load_from_file_long("case2-run1-deg.txt", "\t", 1)
_, case2_run1_compliance = load_from_file("case2-run1-obj.txt", "\t", 0)
case2_run2_time, _, case2_run2_loss = load_from_file_long("case2-run2-deg.txt", "\t", 1)
_, case2_run2_compliance = load_from_file("case2-run2-obj.txt", "\t", 0)
case2_run3_time, _, case2_run3_loss = load_from_file_long("case2-run3-deg.txt", "\t", 1)
_, case2_run3_compliance = load_from_file("case2-run3-obj.txt", "\t", 0)

def plot_compare(title, axis, data_x, data_y1, data_y2, data_y3):
    plot_fig(axis, data_x, data_y1, 's', 'blue', 'D = 0.001', 1.0, 'black', 5)
    plot_fig(axis, data_x, data_y2, 'o', 'red', 'D = 0.01', 1.0, 'black', 5)
    plot_fig(axis, data_x, data_y3, 'D', 'green', 'D = 0.05', 1.0, 'black', 5)
    axis.set_title(title)


plot_compare("Case 1", ax[0][0], case1_run1_time, case1_run1_loss, case1_run2_loss, case1_run3_loss)
plot_compare("Case 2", ax[0][1], case2_run1_time, case1_run1_loss, case2_run2_loss, case2_run3_loss)

plot_compare("", ax[1][0], case1_run1_time, 1/case1_run1_compliance, 1/case1_run2_compliance, 1/case1_run3_compliance)
plot_compare("", ax[1][1], case2_run1_time, 1/case2_run1_compliance, 1/case2_run2_compliance, 1/case2_run3_compliance)

ax[0][0].set_ylabel("Mass loss (%)")
ax[1][0].set_ylabel("Stiffness")
ax[1][0].set_xlabel("Time (nondimentional)")
ax[1][1].set_xlabel("Time (nondimentional)")

handles, labels = ax[0][0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3)

plt.tight_layout()
fig.subplots_adjust(bottom=0.11)
plt.savefig('degradation_stiffness.png', dpi=300)
plt.show()
