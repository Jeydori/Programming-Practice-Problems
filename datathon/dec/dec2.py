#Selection Problem 1

numItems = int(input('Enter the number of items: '))
prices = input('Enter the prices of each item separated by a space: ')
sPrices = prices.split()
iPrices = (int(price) for price in sPrices)

total = sum(iPrices)

if total > 50:
    total = total*(1-0.1)

print('Total Cost is', total, 'php')


