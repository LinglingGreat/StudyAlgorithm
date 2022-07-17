import sys
line = sys.stdin.readline().strip()
res = ""
last = []
i = 0
while i < len(line):
    if line[i] == "i":
        while i < len(line) and line[i] == "i":
            if res:
                res = res[:-1]
            i += 1
    elif line[i] == "o":
        k = i-1
        while i < len(line) and line[i] == "o":
            if k >= 0 and line[k] == "i":
                res = last.pop()
                k -= 1
            else:
                res = res[:-1]
            i += 1
            last.append(res)
    else:
        while i < len(line) and line[i] not in ['i', 'o']:
            res += line[i]
            i += 1
            last.append(res)
    print(line[:i], res)
print(res)
