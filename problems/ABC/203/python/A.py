
abc = list(map(int, input().split()))
new_abc = sorted(abc)

if new_abc[0] == new_abc[1]:
    print(new_abc[2])
elif new_abc[1] == new_abc[2]:
    print(new_abc[0])
else:
    print("0")
