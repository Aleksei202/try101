print('Lesson_4.3.1')

clothes = ['socks', 'shirt', 'skirt', 'scarf']


def insert_element(new_cloth='', index=0):
    clothes.insert(index, new_cloth)
    print(clothes)


insert_element('hat', 2)
insert_element('hat', -2)
insert_element(new_cloth='hat')

print('Lesson_4.3.2')

employee_shift = ['Mark', 'Andrew', 'Emma', 'Kelly', 'John', 'Brad']


def replace_employee(old_employee, new_employee):
    old_person = employee_shift.index(old_employee)
    employee_shift.remove(old_employee)
    employee_shift.insert(old_person, new_employee)
    print(employee_shift)


replace_employee(old_employee='Kelly', new_employee='Maria')

