# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

x = 1
y = 1
z = 1
n = 2

res = []
for i in range(0, x+1):
    print(f"level i {i}")
    for j in range(0, y+1):
        print(f"level j {j}")
        for k in range(0, z+1):
            print(f"level k {k}")
            if i+j+k != n:
                item = res.append([i, j, k])
                print(f"appending {i,j,k}")
                
            else:
                print(f'Cant add {i,j,k}')

print(res)

res2 = [[i,j,k] 
        for i in range(0,x+1) 
        for j in range(0,y+1) 
        for k in range(0,z+1)
        if i+j+k !=n]

print(res2)