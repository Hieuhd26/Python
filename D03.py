#1 Nhập n, nhân n lên 3 rồi cộng 1, rồi in ra màn hình
#2 nhập n, hãy mũ 2 rồi chia cho 3, in kết quả ra màn hình
#3 nhập độ C in ra độ F
#4 Nhập vào số nguyên a, nếu a chia hết cho 2 thì in ra true, ngược lại in false
#5 In ra true nếu a số chia hết cho 3 và nằm trong khoảng từ 50-100, ngược lại in ra false
#a = int(input("Nhập a: " ))
#print(a % 3 ==0 and 50 <= a <=100)
#6 In true nếu a là số chia hết cho 5 nhưng không nằm trong khoảng 20 - 70, ngược lại in false
#7 Nhập vào 2 số nguyên a, b, nếu 1 trong 2 số chia hết cho 2 thì in true, ngược lại thì in false
#8 Nhập vào số thực b, kiểm tra b có phải là số nguyên hay không
'''
b= float(input())
c = round(b)
print(b==c)
'''
#9 nhập số a kiểm tra có phải là số chính phương hay không
'''
a = int(input())
canA = a**0.5
print(canA)
print(canA== round(canA))
'''
#10 Nhập vào lương, đưa cho vợ hết 90% lương, in số tiền lương còn giữ lại
'''
luong = int(input())
print(luong * 0.1)
'''
#11 nhap 3 so va tính tổng
#12 nhap vao a,b,c. Tính d =(a+b)^c. kt xem d có nằm trong khoang 100 -200 không

#dùng if
#13 nhap a, nếu a là số lớn hơn 10 thì in ra dãy "là số lớn hơn 10"
#14 nhap so nguyen dương a, kiem tra a là số chẵn hay lẻ
#14 nhâp a,b,c kiem tra a,b,c co tao thanh 1 tam giac hay khong
#15 nhâp a,b,c kiem tra a,b,c co tao thanh 1 tam giac gi
'''
a = int(input())
b = int(input())
c = int(input())
if (a + b > c and a+c>b and b+c>a):
    if(a== b == c):
        print("tam giac deu")
    elif(a==b or a==c or b==c):
        if(a**2 == b**2+c**2 or b**2 == a**2+c**2 or c**2 == b**2+a**2):
            print("tam giac vuong can")
        else:
            print("tam giac can")
    elif(a**2 == b**2+c**2 or b**2 == a**2+c**2 or c**2 == b**2+a**2):
        print("tam giac vuong")
    else:
        print("tam giac thuong")
else:
    print("a,b,c khong tao thanh mot tam giac")
'''
#16 nhap a,b,c. sap xep a,b,c theo thu tu tang dan
'''
a = int(input())
b = int(input())
c = int(input())
if(a>b):
    a,b=b,a
if(a>c):
    a,c=c,a
if(b>c):
    b,c=c,b
print(a,b,c)
'''
#17 giai va bien luan pt ax+b=0
'''
a = int(input())
b = int(input())
print("pt" + str(a) + " va" + str(b) +": ") 
if(a==0):
    if(b==0):
        print("pt vo so nghiem")
    else:
        print("pt vo nghiem")
else:
    print("nghiem cua pt là: ", (-b/a))
    '''
#18 giai va bien luan pt ax^2 + bx +c =0 bai 19
#vo nghiem: 10 2 10
#nghiem kep: 1 2 1
#2 nghiem: 1 6 5
'''
a = int(input())
b = int(input())
c = int(input())
if(a==0):
    if(b==0):
        if(c==0):
            print("pt có vô số nghiệm")
        else:
            print("pt vô nghiệm")
    else:
        print("pt có nghiệm là: ", -c/b)
else:
    delta = b**2 - 4*a*c
    if delta >0:
        candelta = delta**0.5
        x1 = (-b+candelta)/(2*a)
        x2 = (-b-candelta)/(2*a)
        print("pt co hai nghiem phan biet", x1," ", x2)
    elif delta ==0:
        print("pt co mot nghiem kep la: ", -b/(2*a))
    else:
        print("pt vo nghiệm")
'''            
#19 nhap tháng, năm. Cho biết tháng đso có bao nhiêu ngày
thang = int(input())
nam = int(input())
if(thang != 2):
    if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
        print("tháng ", thang, " năm ", nam, " có: 31 ngày")
    else:
        print("tháng ", thang, " năm ", nam, " có: 30 ngày")
else:
    if(nam % 400 ==0 or (nam % 4==0 and nam % 100 !=0)):
        print("tháng ", thang, " năm ", nam, " có: 29 ngày")
    else:
        print("tháng ", thang, " năm ", nam, " có: 28 ngày")
# tối ưu dùng if elif else

#20 nhap vao ngay, thang. Tính từ ngày nhập đó đến đầu năm cách báo nhiêu ngày
# hai so lien tiep lech 1 thi tru 1 di thoi