import time

a,b,c = 4,5,6


# 3 ta bir xil False False False
# agar istalgan 2 ta ozg qiymati bir xil bolsa natija False
# brortasi 0 ga teng bolsa True 
bosh_vaqti = time.time()
for i in range(10000):
    if a > 0:
        if a == b == c :
            print('False False False')
        elif a==b or b==c or a==c:
            print(False)
        elif a==0 or b==0 or c==0:
            print(True)
        else:
            print(True,True,True)
    else:
        if a==0:
            print('a soni nolga teng')
        else:
            print('a soni manfiy')
oxir_vaqti = time.time()

print(oxir_vaqti - bosh_vaqti)