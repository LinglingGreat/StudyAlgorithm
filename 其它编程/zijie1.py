import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    line = sys.stdin.readline().strip()
    m = len(line)
    wordlist = []
    j = 0
    while j < m:
        k = j
        if line[k:k+2].isupper():
            k += 2
            while k < m and line[k].isupper():
                k += 1
            k -= 1
        elif line[k].isupper():
            k += 1
            while k < m and line[k].islower():
                k += 1
        else:
            while k < m and  line[k].islower():
                k += 1
        wordlist.append(line[j:k].lower())
        j = k
    print("_".join(wordlist))

