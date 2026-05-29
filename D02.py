#tim chuoi con co tong lon nhat
'''
def max_subarray(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

arr = [-2, 11, -4, 13, -5, 2]
print(max_subarray(arr))  # Output: 20
arr1 = [-90, 1, 3, -2, 5, -1, 2, 5, -3]
'''
def liet_ke_cac_cap_thu_cong(arr):
    n = len(arr)
    # Vòng lặp thứ nhất chạy từ đầu đến kế cuối
    for i in range(n):
        # Vòng lặp thứ hai chạy từ phần tử ngay sau i đến hết mảng
        
        #in các cặp phần tử, có trùng
        #for j in range(n):
        #hoặc
        #for j in range(0, n):
        
        #
        for j in range(i + 1, n):
            print(arr[i], " ", arr[j])



def count_target(arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if((arr[i] + arr[j]) % target == 0):
                count = count +1
                print(i, " ", j)
    return count

arr = [1,3,2,6,2]
print(count_target(arr, 4))
    
