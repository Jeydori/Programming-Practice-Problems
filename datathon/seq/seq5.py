#Sequential Problem 5

name = input('Enter your name: ')
age = int(input('Enter your age: '))

if age >= 18:
    print(name, ', you are eligible to vote')
else:
    print(name, ', you are not eligible to vote yet')