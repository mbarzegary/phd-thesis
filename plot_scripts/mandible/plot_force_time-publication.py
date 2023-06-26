from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))

time, force_jaw, force_5, force_4, force_2 = load_from_file_all("force_time.csv", ",", 1)

plot_fig(ax, time, force_jaw, 'D', 'orange', 'Loading on jaw plate', 1.0, None, 6, 'None')
plot_fig(ax, time, force_5, '^', 'red', 'Strength (5 screws)', 1.0, None, 8, 'None')
plot_fig(ax, time, force_4, '^', 'green', 'Strength (4 screws)', 1.0, None, 8, 'None')
plot_fig(ax, time, force_2, '^', 'blue', 'Strength (2 screws)', 1.0, None, 8, 'None')
# plot_fig(ax, disp_28, force_28, None, 'red', '28 days', 1.0, 'black', 5)
# plot_fig(ax, disp_77, force_77, None, 'green', '77 days', 1.0, 'black', 5)
# plot_fig(ax, disp_124, force_124, None, 'purple', '124 days', 1.0, 'black', 5)
# plot_fig(ax, disp_170, force_170, None, 'orange', '170 days', 1.0, 'black', 5)
# ax.set_title("Title")

ax.set_ylim(180, 450)
ax.set_xlim(-2, 175)
ax.set_ylabel("Force (N)")
ax.set_xlabel("Time after implantation [days]")
# axes.yaxis.set_major_locator(MultipleLocator(50))
# axes.yaxis.set_minor_locator(MultipleLocator(50))
ax.legend(loc="bottom right")

plt.tight_layout()
plt.savefig('force_time.png', dpi=300)
plt.show()
