danh_sach = list(map(int, input().split()))
new = {}
for key in range(len(danh_sach)):
    if danh_sach[key] in new:
        new[danh_sach[key]].append(key)
    else:
        new[danh_sach[key]] = [key]
print(new)
        