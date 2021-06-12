NK = list(map(int, input().split()))
ans = 0

for i in range(1,NK[0]+1):
    for j  in range(1,NK[1]+1):
        a = str(i)
        b = str(j)
        c = int(a + "0" + b)
        ans += c

print(ans)
