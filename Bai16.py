ten_file = input()
f = open(ten_file, "r")
dem = 0
for dong in f:
    dem += 1
f.close()
print(dem)