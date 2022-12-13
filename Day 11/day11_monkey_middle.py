class Monkey():

    def __init__(self, name, items, operator, operand, test):
        self.name = name
        self.items = items
        self.operator = operator
        self.operand = operand
        self.divide = int(test)
        self.inspected = 0
        self.monkeyA = None
        self.monkeyB = None
    
    def set_throw_to_monkeys(self, mA, mB):
        self.monkeyA = mA
        self.monkeyB = mB
    
    def operation(self, old, mod=None):
        new = 0

        if self.operator == "*":
            if self.operand == "old":
                new = old * old
            else:
                new = old * self.operand
        else:
            if self.operand == "old":
                new = old + old
            else:
                new = old + self.operand
            
        if mod == None:
            return new // 3
        else:
            return new % mod
    
    def testing(self, item):
        if self.monkeyA == None or self.monkeyB == None:
            print("Please set monkeys to receive throwing items first")
            return -1
        
        if item % self.divide == 0:
            self.monkeyA.items.append(item)
        else:
            self.monkeyB.items.append(item)

    def list_items(self):
        print(f"{self.name}: {self.items}")

    def start_round(self, mod=None):
        for item in range(len(self.items)):
            self.items[item] = self.operation(self.items[item], mod)
            self.testing(self.items[item])
            self.inspected += 1

        self.items = []

def get_data():
    with open("Day 11\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_11_function(verbose=False, part="PartI"):
    monkeys = get_data()
    monkeys = list(map(strip_breaks, monkeys))
    attrs = []
    i = 0

    for line in monkeys:
        if "Monkey" in line:
            attrs.append([line.rstrip(":")])
        elif "Starting items:" in line:
            attrs[i].append(line[16:])
        elif "Operation" in line:
            line = line.split()
            attrs[i].append([line[4], line[5]])
        elif "Test" in line:
            attrs[i].append(line.split()[3])
        elif "If true" in line or "If false" in line:
            attrs[i].append(line[-1])
        
        if "If false" in line:
            i += 1

    monkey_list = []
    for mon in attrs:
        items = list(map(int, map(strip_breaks, mon[1].split(","))))
        operand = int(mon[2][1]) if mon[2][1].isdecimal() else "old"
        monkey = Monkey(mon[0], items, mon[2][0], operand, int(mon[3]))
        monkey_list.append(monkey)
    
    for i, mon in enumerate(monkey_list):
        mA, mB = int(attrs[i][-2]), int(attrs[i][-1])
        mon.set_throw_to_monkeys(monkey_list[mA], monkey_list[mB])
    
    if part == "PartI":
        for r in range(20):
            for mon in monkey_list:
                mon.start_round()
            if verbose:
                print(f"Round {r+1}: ")
                for mon in monkey_list:
                    mon.list_items()
                print()
    else:
        mod = 1
        for mon in monkey_list:
            mod *= mon.divide

        for r in range(10000):
            for mon in monkey_list:
                mon.start_round(mod=mod)
            if verbose:
                print(f"Round {r+1}: ")
                for mon in monkey_list:
                    mon.list_items()
                print()
    
    for mon in monkey_list:
        print(f"{mon.name}: inspected items {mon.inspected} times")

    print()
    items_inspected = []
    for mon in monkey_list:
        items_inspected.append(mon.inspected)
    items_inspected.sort()

    return items_inspected[-1]*items_inspected[-2]

if __name__ == "__main__":
    x = day_11_function()
    print(x)

    print()

    x = day_11_function(part="PartII")
    print(x)