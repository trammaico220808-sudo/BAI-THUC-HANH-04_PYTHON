danh_sach = list(map(int, input().split()))
new = []
for i in danh_sach:
    if i % 2 == 0 or i > 10:
        new.append(i)
print(new)