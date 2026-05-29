'''
import sys

# Đọc một dòng, chuyển thành số nguyên
n = int(sys.stdin.readline())

# Xử lý logic...
result = n * 2

# In kết quả (dùng sys.stdout.write sẽ nhanh hơn print thông thường)
sys.stdout.write(str(result) + '\n')

print(5/3)
print(5%3)
age = 65
a= chr(age)
print(type(age))
print(a)

print(format(10/3,'.2f'))

number =int(input())
for i in range(1,number +1):
    if(i%2==0):
        print(i, end= ' ')

name = "Nguyễn Trung Hiệu"
print(list(name))
'''