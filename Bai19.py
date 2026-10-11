with open("newfile.txt", "r", encoding="utf-8") as f:
     so = [int(dong.strip()) for dong in f if dong.strip()]
khong_trung = set(so)
lon_nhat = max(so)
nho_nhat = min(so)
trung_binh = sum(so)/ len(so)
ket_qua = khong_trung, lon_nhat, nho_nhat,trung_binh
print(ket_qua)