import os

print(os.getcwd())

path = 'C:\Code\opencv\data.txt'
fp = open(path)
str = fp.read()
print(str, end='')
fp.close()