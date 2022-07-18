from helpers import *

# fig = plt.figure(figsize=(10,6))
# ax = fig.add_axes([0.1,0.1,0.5,0.8])
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(13,5))

data_rt = load_from_file_long("kinetic-rt.csv", ",", 1)
data_37 = load_from_file_long("kinetic-37.csv", ",", 1)

''' csv columns:
0: pH
1: Mg2+
2: Cl-
3: Ca2+
4: CaCl+
5: OH-
6: Ca5(PO4)3OH(s)
7: Mg(OH)2(s)
8: Mg3(PO4)2(s)
9: MgCO3(s)
'''

labels = [r'$Mg^{2+}$', r'$Cl^{-}$', r'${Ca}^{2+}$', r'${CaCl}^{+}$', r'${OH}^{-}$',
          r'${Ca}_{5}\left({PO}_{4}\right)_{3} {OH}$', r'${Mg}({OH})_{2}$',
          r'${Mg}_{3}\left({PO}_{4}\right)_{2}$', r'${MgCO}_{3}$']

for i in range(data_rt.shape[1]-1):
    ax[0].plot(data_rt[:,0], data_rt[:,i+1], linewidth=3, label=labels[i])
ax[0].set_title("RT")

for i in range(data_37.shape[1]-1):
    ax[1].plot(data_37[:,0], data_37[:,i+1], linewidth=3, label=labels[i])
ax[1].set_title("37$^{\circ}$C")

for axes in ax.flat:
    axes.set_xlim(4.0, 13.0)
    axes.set_ylim(1e-10, 1e-5)
    axes.set_xlabel("Local pH")
    axes.set_ylabel("Concentration ($g / mm^3$)")
    # axes.yaxis.set_major_locator(MultipleLocator(50))
    # axes.yaxis.set_minor_locator(MultipleLocator(50))
    axes.set_yscale("log")
    # axes.legend()

handles, labels = ax[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=9)

plt.tight_layout()
fig.subplots_adjust(bottom=0.2)
plt.savefig('medusa_profiles.png', dpi=300)
plt.show()
