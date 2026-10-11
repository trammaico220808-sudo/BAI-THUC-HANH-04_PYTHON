with open("scores.txt", "r", encoding="utf-8") as f:
    ds = []
    for dong in f:
        ten, diem = dong.split()
        diem = int(diem)
        ds.append((ten, diem))
    print(ds)
tong_diem = {}
so_lan = {}
for ten, diem in ds:
    if ten not in tong_diem:
        tong_diem[ten] = diem
        so_lan[ten] = 1
    else:
        tong_diem[ten] += diem
        so_lan[ten] += 1
trung_binh = {}
for ten in tong_diem:
        trung_binh[ten] = tong_diem[ten] / so_lan[ten]
print(trung_binh)
with open("result.txt", "w", encoding="utf-8") as f:
     for ten in trung_binh:
          f.write(ten + ": " + str(trung_binh[ten])+ "\n")