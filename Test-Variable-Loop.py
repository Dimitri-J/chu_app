import random
for x in range(0, 9):
    globals()['string%s' % x] = x+2

x = random.randint(1,8)
value_rh = ('rh%s' % x)


print (globals()['string%s' % x])