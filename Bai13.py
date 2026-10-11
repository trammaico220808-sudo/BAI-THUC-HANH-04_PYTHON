so = int(input())
danh_sach = []
for i in range(so):
    a, b = map(int, input().split())
    danh_sach.append((a, b))
new = {}
for a, b in danh_sach:
    if a in new:
        new[a] += b
    else:
        new[a] = b
print(list(new.items()))