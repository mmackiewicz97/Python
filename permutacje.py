import itertools
min_length=8
max_length=8
chrs='qwertyuiopasdfghjklzxcvbnm1234567890'
output = open('pass.txt', 'w')
for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
output.close()
