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
        with open('xchangelog.csv', 'w+') as f:
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


        





c1 = Colony()
for i in range(100000):
    c1.random_interaction()
print(c1.index)
