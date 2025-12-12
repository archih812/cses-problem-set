def can_empty_piles(a, b):

    # check if total is divisible by 3
    if (a + b) % 3 != 0:
        return False
    
    # check if neither pile is more than twice the other
    if 2*a < b or 2*b < a:
        return False
    
    return True

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    print("YES" if can_empty_piles(a, b) else "NO")
