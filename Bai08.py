danh_sach = list(input().split())
so_lan_xuat_hien = {}
for i in danh_sach:
    if i in so_lan_xuat_hien:
        so_lan_xuat_hien[i] += 1
    else:
        so_lan_xuat_hien[i] = 1
print(so_lan_xuat_hien)