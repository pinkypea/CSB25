'''1. Lý thuyết'''
# Khai báo stack bằng list
stack = [1, 2, 3, 4]
# Xem phần tử cuối cùng của stack
print(stack[-1])

# Đưa phần tử vào stack
stack.append(5)
print(stack)

# Xóa phần tử khỏi stack
stack.pop()
print(stack)

stack_length = len(stack)

def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
    
'''2. Thực hành:'''
# Đề bài: Chuyển đổi số thập phân sang nhị phân
# Viết một hàm sử dụng stack để chuyển một số nguyên không âm từ hệ thập phân sang hệ nhị phân.

number = int(input("Nhập số hệ thập phân: "))

def decimal_to_binary(number):
    if number <= 0:
        return 0
    else:
        stack = []
        while number > 0:
            remainer = number % 2
            stack.append(remainer)
            number = number // 2

        result = ""
        while len(stack) > 0:
            remainer = stack.pop()
            result += str(remainer)
        return result

print(decimal_to_binary(number))

# Đề bài: Bạn là 1 lập trình viên đang dựng ứng dụng web đơn giản. Bạn cần phát triển 2 tính năng:
#         - Back: Quay lại web trước đó
#         - Forward: Tiến tới trang web bạn vừa quay lại
class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f"URL: {url}")

    def back(self):
        if self.back_stack:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            previous_page = self.back_stack[-1]
            print(f"Previous page: {previous_page}")
        else:
            print("Nothing to back")

    def forward(self):
        if self.forward_stack:
            forward_page = self.forward_stack.pop()
            self.back_stack.append(forward_page)
            print(f"Forward page: {forward_page}")
        else:
            print("Nothing to forward")

browser = Browser()
browser.visit_page("www.facebook.com")
browser.visit_page("www.youtube.com")
browser.visit_page("www.wikipedia.org")

browser.back()
browser.back()

browser.forward()
browser.forward()
