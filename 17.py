f = open('1_17.txt')
s = f.readlines()
a = 0
m = 0
for i in s:
    x = int(i)
    if 9 < x < 100:
        m = max(m, x)
for i in range(int(s[0])):
    if ((len(s[i]) == 2 and len(s[i + 1]) == 1) or (len(s[i]) == 1 and len(s[i + 1]) == 2)) and (
            s[i] + s[i + 1] == m):
        a += 1
print(a)
