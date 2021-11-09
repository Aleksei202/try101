list = []
f_number = int(input('Enter a number of factorial'))
for i in range(1, f_number + 1):
    list.append(i)

print(list)
factorial = 1
for x in list:
    factorial = factorial * x

print('Factorial =', factorial)