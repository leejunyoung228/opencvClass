import os
os.system('cls')

nation = {'Korea':"+82", 'US':"+1", 'Japan':"+81"}

print(nation['Korea'])

var = input()

if var in nation:
    print('country code =', nation[var])
else:
    print('somthing wrong~~~!!!!')