#Sequential Problem 4

celciusS = int(input('Input a starting temperature in Celcius:'))
celciusE = int(input('Input an ending temperature in Celcius:'))
num = 0

while num < celciusS:
    farenheit = (9/5)*celciusS+32
    print('Celcius =', celciusS, '|', 'Farenheit', farenheit)
    celciusS += 1

    if celciusS == celciusE+1:
        break
