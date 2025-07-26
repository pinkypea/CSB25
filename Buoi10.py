'''1. Kiểu dữ liệu set'''
# Khai báo set
fruit_basket = {"apple", "banana", "cherry", "apple"}

# Truy cập các phần tử trong set bằng for
for fruit in fruit_basket:
    print(fruit)

# Thêm phần tử mới vào trong set
fruit_basket.add("orange")
fruit_basket.update({"kiwi", "peach"})

# Xóa phần tử khỏi set
fruit_basket.remove("apple")
fruit_basket.discard("apple")

# Phép hợp trong set
lunch = {"soup", "sandwich", "omelet"}
dinner = {"soup", "steak", "ice-scream"}
#O(m + n)
meals = lunch.union(dinner)
meals = lunch | dinner

# Phép giao trong set
laptop = {"lenovo", "apple", "dell"}
tablet = {"apple", "lenovo", "samsung"}
devices = laptop.intersection(tablet)
devices = laptop & tablet

# Phép trừ trong set
car = {"mercedes", "vinfast", "bmw"}
motobike = {"honda", "yamaha", "vinfast"}
transportations = car.difference(motobike)
transportations = car - motobike

'''2. Ánh xạ'''
gpa_10 = [5.0, 7.0, 10.0, 9.0]
def convert_gpa(score):
    return score/10 * 4

gpa_4 = map(convert_gpa, gpa_10)
print(list(gpa_4))


students = ["Hieu", "My Anh", "Tuan Anh"]
students_upper = map(str.upper, students)
print(list(students_upper))

'''3. Kiểu dữ liệu Dictinary'''
person = {
    "name": "Kien",
    "gender": "Male",
    "age": 20,
    "job": "Engineer"
}
person["age"] = 50
person["hometown"] = "Hanoi"

# Khởi tạo dictinary
phone_book = {}
phone_book = dict()

# Thêm/Cập nhật dictionary
phone_book['John'] = '0123456789'
phone_book['Alice'] = '9876543210'

# Truy xuất dictionary
print(phone_book.get("John"))

# Xóa value trong dictionary
del phone_book["Alice"]