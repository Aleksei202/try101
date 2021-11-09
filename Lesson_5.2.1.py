x = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print('numbers in list')
for number in x:
    print(number)

print('numbers and square of numbers in list')
for number in x:
    print(number)
    print(number * number)

print('numbers +"total" variable in list')
total = 0
for number in x:
    print(number + total)
print('total=', total)

print('product of list')
product = 1
for number in x:
    product *= number
print('product=', product)
