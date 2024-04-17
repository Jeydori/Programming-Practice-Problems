#Repititive Problem 2

number = int(input('Enter a number: '))

print('M U L T I P L I C A T I O N T A B L E')

if number >= 1:
    for num in range(1, 11):
        mult = number*num
        print(number, '*', num, ' = ', mult)