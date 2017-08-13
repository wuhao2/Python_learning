import random

ant_point = random.randint(0,20)
worm_point = random.randint(0,20)
print('ant_point:',ant_point,' worm_point:',worm_point)

step = [-2,+2,-3,+3]

while ant_point != worm_point:
    astep = random.choice(step)
    if 0 <= ant_point + astep <= 20:
        ant_point += astep

    astep = random.choice(step)
    if 0 <= worm_point + astep <= 20:
        worm_point += astep
    print('ant_point:',ant_point,' worm_point:',worm_point)
