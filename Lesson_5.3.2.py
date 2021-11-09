numbers = []


def print_sum_avg(*args):
    print(sum(args))
    print((sum(args)) / 3)


for i in range(0, 3):
    number = int(input(f'Enter value {i} of list: '))
    numbers.append(number)

print("Numbers list", numbers)

print_sum_avg(numbers)
