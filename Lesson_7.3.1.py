class Zoo:
    def __init__(self, animals, employees):
        self.animals = animals
        self.employees = employees

    def __str__(self):
        return 'Animals in zoo ' + str(self.animals) + ' Employees ' + str(self.employees)

    def add_animal(self):
        names = 0
        for element in self.employees:
            names += 1
        if self.animals['quantity'] / names > 10:
            print("Not enough employees! Can't care about a new animal.")
        else:
            self.animals['quantity'] = self.animals['quantity'] + 1
            if self.animals['quantity'] / names > 10:
                print("Not enough employees! Hire someone new.")

    def remove_animal(self):
        self.animals['quantity'] = self.animals['quantity'] - 1

    def hire_new_employee(self, name):
        self.employees.append(name)

    def fire_employee(self):
        self.employees.pop(-1)


zoo1 = Zoo({'animals': 'squirrel', 'quantity': 3}, ['John'])
zoo1.add_animal()
print(zoo1)
zoo1.remove_animal()
print(zoo1)
zoo1.hire_new_employee('Sam')
print(zoo1)
zoo1.fire_employee()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.hire_new_employee('Sam')
print(zoo1)
zoo1.add_animal()
print(zoo1)
zoo1.add_animal()
print(zoo1)