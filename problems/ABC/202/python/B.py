S = input()

rS = S[::-1]

ans = ''
for i in rS:
    a = i
    if i == '6':
        a = '9'
    elif i == '9':
        a = '6'
    ans += a

print(ans)
