'''
def sinh_nhi_phan_quay_lui(n):
    # Mảng để lưu cấu hình nhị phân hiện tại
    X = [0] * n
    def backtrack(i):
        # Duyệt qua các giá trị có thể nhận tại vị trí i (0 và 1)
        for val in [0, 1]:
            X[i] = val  # Thử gán giá trị
            # Nếu đã điền xong vị trí cuối cùng (i == n - 1)
            if i == n - 1:
                print("".join(map(str, X)))  # In ra cấu hình tìm được
            else:
                backtrack(i + 1)  # Gọi đệ quy để điền tiếp vị trí i + 1

    # Bắt đầu quay lui từ vị trí đầu tiên (chỉ số 0)
    backtrack(0)

# Chạy thử với n = 3
print("Các xâu nhị phân độ dài 3:")
sinh_nhi_phan_quay_lui(3)
'''
#x = [1,2,3]
#print(list(map(str,x)))

#import itertools
#print(list(itertools.combinations(range(1, 6), 3)))
def inkq():
    # In từ phần tử thứ 1 đến k (bỏ qua phần tử 0)
    print(X[1:])

def Try(i):
    global n, k, X
    
    # Cận dưới: X[i-1] + 1
    # Cận trên trong Python: range(start, stop) sẽ chạy đến stop - 1. 
    # Vì thế ta phải cộng thêm 1 vào cận trên: (n - k + i) + 1 = n - k + i + 1
    lower_bound = X[i - 1] + 1
    upper_bound = n - k + i + 1
    
    for j in range(lower_bound, upper_bound):
        X[i] = j  # Ghi nhận giá trị
        
        if i == k:
            inkq()  # Đủ k phần tử thì in kết quả
        else:
            Try(i + 1)  # Chưa đủ thì tìm tiếp cho vị trí i + 1

# --- Chương trình chính ---
n = 5
k = 3

# Khởi tạo mảng X có kích thước k + 1, phần tử X[0] = 0 làm lề
X = [0] * (k + 1)

print(f"Các tổ hợp chập {k} của {n} là:")
Try(1)  # Bắt đầu thử từ vị trí thứ 1
