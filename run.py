from colony import Colony
from plot import plot
from mlpplot import plot_mpl
from tqdm import tqdm
c1 = Colony()
for i in tqdm(range(1, 5000)):
    if i%2500 == 0:
        c1.kill_ants_single_on_command()
    c1.random_interaction()
    c1.add_new_ants()
    c1.kill_ants()
    c1.write_to_file()
print(c1.index)
plot_mpl()

c2 = Colony()
for i in tqdm(range(1, 5000)):
    if i%2500 == 0:
        c2.kill_ants_single_on_command()
    c2.add_new_ants()
    c2.kill_ants()
    c2.write_to_file()
print(c2.index)
plot_mpl()


