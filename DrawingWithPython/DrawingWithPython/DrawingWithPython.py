import sys

for x in range(0, 1000):
    for z in range(x/2, 10):
        sys.stdout.write(" ")
    for y in range(0, x):
        sys.stdout.write("*")
    sys.stdout.write("\n")
    x = x - 1