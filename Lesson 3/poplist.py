a = [1,4,5,9,55,6,65]
b = len(a)

for i in range(b):
    print(i)
    if i % 2 !=0:
        a.pop(i)
        print(a)
print(a)