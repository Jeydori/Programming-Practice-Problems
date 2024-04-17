# Sequential 1
name = input('Input your name: ')
age = int(input('Input your age: '))

if age < 13:
    print(name, 'you are a child')
elif age < 19:
    print(name, 'you are a teenager')
elif age < 65:
    print(name, 'you are an adult')
else:
    print(name, 'you are a senior')