f = open('1_24.txt')
s = f.readline()
a = 0
maxx = 0
for i in range(len(s) - 1):
    if i != len(s) and i != 0:
        if s[i] == s[i - 1] == 'A' or s[i] == s[i + 1] == 'A':
            a = 0
        elif s[i] == s[i - 1] == 'B' or s[i] == s[i + 1] == 'B':
            a = 0
        elif s[i] == s[i - 1] == 'C' or s[i] == s[i + 1] == 'C':
            a = 0
        else:
            a += 1
            if a > maxx:
                maxx = a
    if i == len(s) - 1:
        if s[i] == s[i - 1] == 'A':
            a = 0
        elif s[i] == s[i - 1] == 'B':
            a = 0
        elif s[i] == s[i - 1] == 'C':
            a = 0
        else:
            a += 1
            if a > maxx:
                maxx = a
    if i == 0:
        if s[i] == s[i + 1] == 'A':
            a = 0
        elif s[i] == s[i + 1] == 'B':
            a = 0
        elif s[i] == s[i + 1] == 'C':
            a = 0
        else:
            a += 1
            if a > maxx:
                maxx = a
print(maxx)
