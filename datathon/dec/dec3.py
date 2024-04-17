#Selection Problem 2

score= int(input('Enter your score: '))

if score < 60:
    print('Your corresponding letter grade is F')
elif score < 70:
    print('Your corresponding letter grade is E')
elif score < 80:
    print('Your corresponding letter grade is D')
elif score < 90:
    print('Your corresponding letter grade is C')
else:
    print('Your corresponding letter grade is A')