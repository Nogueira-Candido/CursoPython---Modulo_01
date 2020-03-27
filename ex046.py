import time, sys

for i in range(10,-1,-1):
   # i -= 10
    sys.stdout.write("  \n{}".format(i))
    sys.stdout.flush()
    time.sleep(1)

print('\nFOGOS EXPLODINDO!!!!')


'''
import time
c = time.sleep(10)
for c in range(1,10):
    print(c)
'''