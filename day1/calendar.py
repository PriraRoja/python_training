  
w = 3
initial = w-1
print('sun mon tue wed thu fri sat')
print(' ' * (initial) * 4), end='')

for var in range(1,32):
    print(f'{var:<3}', end = ' ')
    initial+=1
    if(initial==7):
        initial=0
        print()