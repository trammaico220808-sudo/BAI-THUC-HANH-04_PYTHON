toan = int(input())
van = int(input())
anh = int(input())
ten = input()
dtb = (toan + van + anh)/3
if dtb >= 8:
    loai = "Gioi"
elif dtb >= 6.5:
    loai = "Kha"
elif dtb >= 5:
    loai = "Trung binh"
else:
    loai = "Yeu"
danh_sach = {}
danh_sach[ten] = loai
print(danh_sach)