class Zoo:
    def __init__(self, animals, employees):
        self.animals = animals
        self.employees = employees

    def __str__(self):
        return 'Animals in zoo ' + str(self.animals) + ' Employees ' + str(self.employees)

    def add_animal(self, animal='squirrel', number=1):
        names = 0
        for element in self.employees:
            names += 1
        values = self.animals.values()
        total_animals = sum(values)
        will_total_animals = total_animals + number
        print('total animals=', total_animals, 'will total animals =', will_total_animals)
        if total_animals / names > 10:
            print('Not enough employees!Can not take care about animals!')
        if will_total_animals / names > 10 and total_animals / names < 10:
            if animal not in self.animals.keys():
                self.animals[animal] = number
            else:
                self.animals[animal] = self.animals[animal] + number

            print('Not enough employees for all animals. Hire someone new!')
        if will_total_animals / names < 10:
            if animal not in self.animals.keys():
                self.animals[animal] = number
            else:
                self.animals[animal] = self.animals[animal] + number

    def remove_animal(self, animal, number):
        self.animals[animal] = self.animals[animal] - number

    def hire_new_employee(self, name):
        self.employees.append(name)

    def fire_employee(self):
        self.employees.pop(-1)


zoo1 = Zoo({'squirrel': 3}, ['John'])
print(zoo1)
zoo1.add_animal('tiger', 3)
print(zoo1)
zoo1.add_animal('tiger', 1)
print(zoo1)
zoo1.add_animal('mouse', 10)
print(zoo1)
zoo1.add_animal('mouse', 30)
print(zoo1)
zoo1.remove_animal('mouse', 3)
print(zoo1)
zoo1.hire_new_employee('Sam')
print(zoo1)
zoo1.fire_employee()
print(zoo1)
