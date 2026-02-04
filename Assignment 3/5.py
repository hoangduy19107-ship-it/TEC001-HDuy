s = input('enter a string: ')
if len(s) % 2 != 0:
    s = s[len(s)//2]
    print(s)
else:
    print(s[len(s)//2 - 1], s[len(s)//2])
