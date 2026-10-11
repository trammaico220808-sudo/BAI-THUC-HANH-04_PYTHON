f = open("data.txt", "r")
ds = {}
for dong in f:
    ten, diem = dong.split()
    diem = int(diem)
    if ten not in ds:
       ds[ten] = []
    ds[ten].append(int(diem))

f.close()
print(ds)