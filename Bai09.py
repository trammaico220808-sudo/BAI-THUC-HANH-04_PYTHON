danh_sach1 = {"a": 1, "b": 2, "c":"Hello"}
danh_sach2 = {"d":3, "e":4, "c":"World"}
danh_sach3 = danh_sach1.copy()
for key in danh_sach1:
    if key in danh_sach2:
        danh_sach3[key] = (danh_sach1[key]) + " " + (danh_sach2[key])
    else:
        danh_sach3[key] = danh_sach1[key]
print(danh_sach3)