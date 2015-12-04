import random
with open('piropos.txt') as f:
    lines = f.readlines()
    print random.choice(lines)

#with random.choice(open('piropos.txt')) as f:
#	line = f.readlines()
#	print line

