import time
import os

distance = 100
n = 0
simulation_speed = float(input('Enter simulation speed(0.01 recommended) : '))
input = float(input('Enter distance of the celestial body from earth(in km) : '))
speed_light = 300000
time_sec = input / speed_light
sec = time_sec / distance*2

for i in range(distance):
    for i in range(15):
        print()
    print('     hyphen(-) represents light, C represents Celestial body, E represents Earth \n\n')
    print(f'    It will take {time_sec} seconds for light to reach earth from this distant celestial body.')
    print(end=' C')
    if n > 0:
        for i in range(n):
            print(end='-')
    if n == distance-1:
        print('E')
    else :
        for i in range(distance-n-1):
            print(end=' ')
        if i == distance-n-2:
            print("E")
    n += 1
    time.sleep(simulation_speed)
    os.system('cls')

n = 0

for i in range(distance):
    for i in range(15):
        print()
    print('     hyphen(-) represents light, X represents Dead Celestial body, E represents Earth \n\n')
    print(f'    Celestial body died! But the light of the star will continue to appear on earth for {time_sec} seconds because light travels through the space as a electromagnetic wave and it take a certain amount of time for light to reach certain distances. \n\n')
    print(end=' X')
    if n > 0:
        for i in range(n):
            print(end=' ')
    if n == distance-1:
        print('E')
    else :
        for i in range(distance-n-1):
            print(end='-')
        if i == distance-n-2:
            print("E")
    n += 1
    time.sleep(simulation_speed+0.08)
    os.system('cls')