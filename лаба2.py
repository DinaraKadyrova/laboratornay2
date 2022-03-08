import re
k = int(input('Введите число: '))
with open('laba2.txt','r') as f:
    mass = f.read()
mass=re.split('[!|./?]', mass)
n=0
m=1
for words in mass:
    for char in words:
        if char==' ':
            n=0
        else:
            n+=1
            m=n
    if m>k:
        idx = mass.index(words)
        print(mass[idx])