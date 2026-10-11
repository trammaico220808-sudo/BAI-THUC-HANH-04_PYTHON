danh_sach = list(map(int, input().split()))
moi = []
for i in danh_sach:
    if i not in moi:
        moi.append(i)
print(moi)