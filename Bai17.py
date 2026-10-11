ghi_list_ra_ten_file = [10,20,30,40,50]
f = open("ten_file.txt", "w", encoding="utf-8")
for i in ghi_list_ra_ten_file:
    f.write(str(i) + "\n")
f.close()