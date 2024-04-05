print('The Rice Purity Test is an anonymous online survey that has been taken by millions of people around the world. It was originally developed by Rice University in 1924 as a way to measure the moral character of incoming freshman students.')

total = 0
puritytest = {
    1: 'Held hands romantically?',
    2: 'Been on a date?',
    3: 'Been in a relationship?',
    4: 'Danced without leaving room for Jesus?',
    5: 'Kissed a non-family member?',
    6: 'Kissed a non-family member on the lips?',
    7: 'French kissed?',
    8: 'French kissed in public?',
    9: 'Kissed on the neck?',
    10: 'Kissed horizontally?',
    11: 'Given or received a hickey?',
    12: ' Kissed or been kissed on the breast?',
    13: 'Kissed someone below the belt?',
    14: 'Kissed for more than two hours consecutively?',
    15: 'Played a game involving stripping?',
    16: 'Seen or been seen by another person in a sensual context?',
    17: 'Prayed',
    18: 'Showered with a MPS',
    19: 'Fondled or had your butt cheeks fondled?',
    20: 'Fondled or had your breasts fondled?',
}

for item in puritytest.values():
    response = input(item + " (yes/no): ").lower()
    if response == 'yes':
        total += 1
    elif response != 'no':
        print('Invalid response. Please enter "yes" or "no".')

print(f'Your Rice Purity Test result is {total} out of {len(puritytest)} questions.')
print('Thank you for using the short  game')
