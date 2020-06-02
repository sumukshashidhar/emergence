class Ant:

    def __init__(self, setrole):
        self.role = setrole
        self.batch = 0
        self.memory = {
            "worker": 0,
            "harvester": 0,
            "soldier": 0,
            "caretaker": 0
        }


    def meet(self, other_type):
        self.memory[other_type] += 1
        self.batch += 1
        # print("Batch is now:", self.batch)
        # print("Memory is now:" , self.memory)
        if self.batch >= 10:
            total = 0
            for key in self.memory.keys():
                total += self.memory[key]
            # print(total)
            # print(self.memory)
            min_frac = 100
            curpop = ''
            for key in self.memory.keys():
                current_pop = self.memory[key]
                # percentage calculation and checking whether less than 10% of the ants it has met is
                frac = current_pop / total
                if frac < min_frac:
                    min_frac = frac
                    curpop = key
                # print(frac, key, total, current_pop)
            if min_frac < 0.25:
                to_type = curpop
                # changing the role
                saverole = self.role
                self.role = to_type
                self.batch = 0
                # we need to reset its memory
                self.memory = {
                    "worker": 0,
                    "harvester": 0,
                    "soldier": 0,
                    "caretaker": 0
                }
                    # print("TOTYPECHANGEIS:", saverole, to_type)
        # print("YOU SEE ME ROLLING",self.role)
        return self.role