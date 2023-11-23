f = 0
s = 'АБЗИ'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                f += 1
                if a + b + c + d == 'ИЗБА':
                    print(f)