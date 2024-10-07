def leap_year(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0

def check_valid_date(ngay, thang, nam):
    if thang < 1 or thang > 12 or ngay < 1:
        return False
    if thang in [4, 6, 9, 11] and ngay > 30:
        return False
    if thang == 2:
        if leap_year(nam):
            if ngay > 29:
                return False
        elif ngay > 28:
            return False
    if ngay > 31:
        return False
    return True

def ngay_ke_tiep(ngay, thang, nam):
    ngay += 1
    if check_valid_date(ngay, thang, nam):
        return ngay, thang, nam
    ngay = 1
    thang += 1
    if thang > 12:
        thang = 1
        nam += 1
    return ngay, thang, nam

# Nhập ngày tháng năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if check_valid_date(ngay, thang, nam):
    ngay_moi, thang_moi, nam_moi = ngay_ke_tiep(ngay, thang, nam)
    print(f"Ngày kế tiếp là: {ngay_moi:02d}/{thang_moi:02d}/{nam_moi}")
else:
    print("Ngày không hợp lệ!")