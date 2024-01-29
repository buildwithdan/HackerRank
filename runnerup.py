
n = int(input('your number'))

arr = map(int, input().split())
arr_lst = lst(arr)
arr_set = sorted(set(arr_lst))
# print(arr_set)

runner_up = arr_set[-1]
 
print(runner_up)   
    