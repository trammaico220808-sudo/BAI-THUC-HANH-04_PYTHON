danh_sach = list(map(int, input().split()))
gia_tri_lon_nhat = danh_sach[0]
for i in danh_sach:
    if i > gia_tri_lon_nhat:
        gia_tri_lon_nhat = i
print(gia_tri_lon_nhat)