import sys
r = raw_input("give string:\n")
l = len(r)
i = len(r) - 1
string = ""
for x in range(0, l):
    string = string + r[i]
    i = i - 1
print string
