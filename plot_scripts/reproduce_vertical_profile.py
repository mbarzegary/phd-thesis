from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,6))

x_cp_rt, y_cp_rt = load_from_file("CPMg-HBSS-RT-profile.txt", "\t")
x_cp_37, y_cp_37 = load_from_file("CPMg-HBSS-37-profile.txt", "\t")
x_uhp_rt, y_uhp_rt = load_from_file("UHPMg-HBSS-RT-profile.txt", "\t")
x_uhp_37, y_uhp_37 = load_from_file("UHPMg-HBSS-37-profile.txt", "\t")

plot_fig(ax[0], y_cp_rt, x_cp_rt, 's', 'blue', 'RT')
plot_fig(ax[0], y_cp_37, x_cp_37, 'o', 'red', r'37 $^{\circ}$ C')
ax[0].set_title("CPMg")

plot_fig(ax[1], y_cp_rt, x_cp_rt, 's', 'blue', 'RT')
plot_fig(ax[1], y_cp_37, x_cp_37, 'o', 'red', r'37 $^{\circ}$ C')
ax[1].set_title("UHPMg")

for axes in ax.flat:
    axes.set_xlim(7.3, 8.5)
    axes.set_ylim(0, 550)
    axes.invert_xaxis()
    axes.set_xlabel("Local pH")
    axes.set_ylabel("Height ($\mu m$)")
    axes.yaxis.set_major_locator(MultipleLocator(50))
    # axes.yaxis.set_minor_locator(MultipleLocator(50))
    # axes.legend()

handles, labels = ax[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=2)

plt.tight_layout()
plt.savefig('reproduce_vertical_profile.png', dpi=300)
plt.show()
