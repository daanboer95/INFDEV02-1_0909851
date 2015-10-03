import sys

for x in range(0, 10):
    for z in range(x/2, 10):
        sys.stdout.write(" ")
    for y in range(0, x):
        sys.stdout.write("*")
    sys.stdout.write("\n")
    x = x - 1

sys.stdout.write("\n\n*****************\n\n")


for o in range(0, 10):
    sys.stdout.write("*")
sys.stdout.write("\n")
for p in range(0, 8):
    sys.stdout.write("*")
    for k in range(0, 8):
        sys.stdout.write(" ")
    sys.stdout.write("*")
    sys.stdout.write("\n")
for o in range(0, 10):
    sys.stdout.write("*")

sys.stdout.write("\n\n*****************\n\n")

for x in range(-5, 6):
    for z in range(-abs(x), 1):
        sys.stdout.write("*")
    for y in range(0, ((5-abs(x))*2)):
        sys.stdout.write(" ")
    for z in range(-abs(x), 1):
        sys.stdout.write("*")
    sys.stdout.write("\n")

sys.stdout.write("\n\n*****************\n\n")

for x in range(-5, 6):
    for z in range(-abs(x), 0):
        sys.stdout.write(" ")
    sys.stdout.write("*")
    for y in range(0, ((5-abs(x))*2)):
        sys.stdout.write(" ")
    sys.stdout.write("*")
    sys.stdout.write("\n")

sys.stdout.write("\n\n*****************\n\n")

for x in range(-3, 4):
    if(x>-2 and x<2):
        sys.stdout.write("*")
    else:
        sys.stdout.write(" ")
    for y in range(0, int(2 ** (abs(x)^2 ))):
        sys.stdout.write(" ")
    sys.stdout.write("*")
    sys.stdout.write("\n")

sys.stdout.write("\n\n*****************\n\n")

for x in range(-3, 4):
    for y in range(3, (2 ** abs(x))):
        sys.stdout.write(" ")
    sys.stdout.write("*")
    for y in range(3-(2 ** abs(x)), 3):
        sys.stdout.write(" ")
    sys.stdout.write("*")
    sys.stdout.write("\n")

sys.stdout.write("\n\n*****************\n\n")

for x in range(-3, 4):
    for y in range(0, (2 ** abs(x))):
        sys.stdout.write(" ")
    sys.stdout.write("*")
    sys.stdout.write("\n")
