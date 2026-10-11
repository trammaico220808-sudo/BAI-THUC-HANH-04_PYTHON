danh_sach = list(input().split())
new = []
for i in danh_sach:
    i = i.title()
    if i not in new:
        new.append(i)
print(new)