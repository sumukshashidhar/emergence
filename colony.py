import random
from ant import Ant



class Colony:

    def __init__(self):
        with open('meetlog.csv', 'w+') as x:
            pass
        with open('creation.csv', 'w+') as f:
            pass
        with open('changelog.csv', 'w+') as f:
            pass
        with open('ant_data.csv', 'w+') as f:
            pass
        self.index = {
            "worker": 0,
            "harvester": 0,
            "soldier": 0,
            "caretaker": 0
        }

        self.array = []

        for i in range(100):
            types = ['worker', 'harvester', 'soldier', 'caretaker']
            choice_of_ant = random.randint(0, 3)
            newAnt = Ant(types[choice_of_ant])
            with open('creation.csv', 'a') as f:
                f.write(f'{newAnt.role} \n')
            self.array.append(newAnt)
            self.index[newAnt.role] += 1

        print(self.index)


    def random_interaction(self):
        choice_1 = random.randint(0, len(self.array)-1)
        choice_2 = random.randint(0, len(self.array)-1)

        if choice_1 == choice_2:
            return self.random_interaction()

        else:
            with open('meetlog.csv', 'a') as f:
                f.write(f'{self.array[choice_1].role}, {self.array[choice_2].role} \n')
            saveChoice1 = self.array[choice_1].role
            saveChoice2 = self.array[choice_2].role

            resp1 = self.array[choice_1].meet(self.array[choice_2].role)
            resp2 = self.array[choice_2].meet(self.array[choice_1].role)

            if saveChoice1 != resp1:
                with open('changelog.csv', 'a') as f:
                    f.write(f'{saveChoice1}, {resp1} \n')
                    self.index[saveChoice1] -= 1
                    self.index[resp1] += 1
            if saveChoice2 != resp2:
                with open('changelog.csv', 'a') as f:
                    f.write(f'{saveChoice2}, {resp2} \n')
                    self.index[saveChoice2] -= 1
                    self.index[resp2] += 1


    def kill_ants_single_on_command(self):

        """
        Simulates an environment by killing a random number of ants.

        Select a random ant, save its role, remove it, and update our indexes
        """
        if True:
            ant_types = ['worker', 'harvester', 'soldier', 'caretaker']
            random_type = random.randint(0, 3)
            num_ants_killed = 20
            while num_ants_killed > 0:
                try:
                    for i in range(len(self.array)):
                        if self.array[i].role == ant_types[random_type]:
                            self.index[ant_types[random_type]] -= 1
                            del self.array[i]
                            num_ants_killed -= 1
                        if i == len(self.array) - 1:
                            num_ants_killed = 0
                except IndexError:
                    num_ants_killed = 0

    def write_to_file(self):
        with open('ant_data.csv', 'a') as f:
            f.write(
                f"{self.index['worker']}, {self.index['harvester']}, {self.index['soldier']}, {self.index['caretaker']}, {0.01 * (self.index['worker'] + self.index['harvester'] + self.index['soldier'] + self.index['caretaker'])}\n")

    def add_new_ants(self):
        """
        Adds a random number of ants after each episode
        """
        rand = 10
        for i in range(rand):
            ant_types = ['worker', 'soldier', 'caretaker', 'harvester']
            choice_of_ant = random.randint(0, 3)
            ant_object = Ant(ant_types[choice_of_ant])
            self.index[ant_types[choice_of_ant]] += 1
            self.array.append(ant_object)

    def kill_ants(self):
        """
        Simulates an environment by killing a random number of ants.

        Select a random ant, save its role, remove it, and update our indexes
        """
        num_ants_killed = 5
        for i in range(num_ants_killed):
            killed_ant = random.randint(0, len(self.array) - 1)
            killed_ant_role = self.array[killed_ant].role
            self.index[killed_ant_role] -= 1
            del self.array[killed_ant]






# c1 = Colony()
# for i in range(1, 100000):
#     if i%50000 == 0:
#         c1.kill_ants_single_on_command()
#     c1.random_interaction()
#     c1.write_to_file()
# print(c1.index)
