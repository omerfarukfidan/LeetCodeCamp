my_arr = [8,7,9,2,4,5,65,44,56]

def find_hundred(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i]+arr[i+1] == 100:
            return [arr[i],arr[i+1]]
    return 0

print(find_hundred(my_arr))
