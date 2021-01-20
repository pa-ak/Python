s = '1.23,2.4,3.123'
total = 0

for l in range(0,len(s)):
    if s[l] == ',':
        c = l + 1
        while s[c] != ',':
            c = c + 1
            if s[c] == ',':
                total = total + float(s[l:c])
print (total)