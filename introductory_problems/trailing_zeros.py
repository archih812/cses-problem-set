n = int(input())
res = 0
deno = 5
while True:
    val = n // deno
    if val == 0:
        break
    deno *= 5
    res += val
print(res)
