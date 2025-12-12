dna = input()
curr_len, max_len = 1, 1
curr = dna[0]
for i in range(1, len(dna)):
    if dna[i] == curr:
        curr_len += 1
        max_len = max(max_len, curr_len)
    else:
        curr = dna[i]
        curr_len = 1
print(max_len)