from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,6))

time, rate_high, rate_low = load_from_file("degradation.csv", "\t", 1)

plot_fig(ax, time, rate_high, 's', 'blue', 'Degradation in saline solution', 1.0, 'black', 5)
plot_fig(ax, time, rate_low, 'o', 'red', 'Degradation in buffered solution', 1.0, 'black', 5)
ax.set_title("Biodegradation over time")

ax.set_ylim(0, 80)
ax.set_xlim(0, 50)
ax.set_ylabel("Mass loss (%)")
ax.set_xlabel("Time (hour)")
# axes.yaxis.set_major_locator(MultipleLocator(50))
# axes.yaxis.set_minor_locator(MultipleLocator(50))
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig('degradation_rate.png', dpi=300)
plt.show()
