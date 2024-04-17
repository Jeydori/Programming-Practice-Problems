#Sequential Problem 3

number = input('Input a series of numbers separated by spaces: ')
sNumber = number.split(' ')
print(sNumber)

iNumber = (int(Num) for Num in sNumber)

Average = sum(iNumber)/len(sNumber)

print('Average is equal to', Average)
