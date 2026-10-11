da_nop = (set(map(int, input().split())))
ds_lop = (set(map(int, input().split())))
chua_nop = ds_lop - da_nop
print((da_nop), (chua_nop))