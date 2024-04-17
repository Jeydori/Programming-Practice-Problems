#Selection Problem 5

distance = float(input('Enter a distance in km: '))

if distance <= 1:
    print('with a ', distance, 'km distance, we suggest you to walk')
elif distance <= 10:
    print('with a', distance, 'km distance, we suggest you to ride a bike')
else:
    print('with a', distance, 'km distance, we suggest you to take a public transpo')
