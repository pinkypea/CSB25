# Bài 1 – Stack: Đảo ngược chuỗi
# Thuật toán:
#     - Tạo một stack rỗng.
#     - Duyệt từng ký tự trong chuỗi, push vào stack.
#     - Trong khi stack chưa rỗng: pop từng ký tự và nối vào chuỗi kết quả.
#     - Trả về chuỗi kết quả đã đảo.

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)

    result = ""
    while stack:
        result += stack.pop()
    
    return result

print(reverse_string("MindX"))

# Bài 2 – Stack: Kiểm tra dấu ngoặc hợp lệ (), []
# Thuật toán:
#     - Tạo stack rỗng và bảng ánh xạ bracket_pairs = {')': '(', ']': '[', '}': '{' }.
#     - Duyệt từng ký tự:
#         + Nếu là ngoặc mở -> push vào stack.
#         + Nếu là ngoặc đóng ->
#             Nếu stack rỗng: không hợp lệ.
#             Lấy top = pop() và kiểm tra top == bracket_pairs[ký tự hiện tại]. 
#                 => Nếu sai: không hợp lệ.
#     - Sau khi duyệt xong: hợp lệ nếu stack rỗng.

def is_valid_bracket_pairs(s):
    stack = []
    openning_brackets = '([{'
    closing_brackets = ')]}'
    bracket_pairs = {')':'(', ']':'[', '}':'{'}

    for char in s:
        if char in openning_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    return len(stack) == 0

print(is_valid_bracket_pairs("{[()]}"))
print(is_valid_bracket_pairs("{[(]]}"))

# Bài 3:
# Có một stack vé (vé đặt chồng, phát từ trên xuống).
# Có một queue khách (khách xếp hàng chờ mua).
# Khi bán: khách ở đầu hàng sẽ nhận vé từ trên cùng.
# Kết thúc, kiểm tra:
# Còn bao nhiêu khách không mua được vé?
# Còn bao nhiêu vé chưa được bán?

# Thuật toán:
#     - Lấy một vé từ stack (pop).
#     - Lấy một khách từ queue (popleft).
#     - Lặp lại cho đến khi:
#     - Hết vé hoặc hết khách.
#     - Trả về số vé còn lại trong stack và số khách còn lại trong queue.

from collections import deque
def ban_ve(ticket_stack, customer_queue):

    while ticket_stack and customer_queue:
        ticket_stack.pop()
        customer_queue.popleft()

    return len(ticket_stack), len(customer_queue)

tickets = ["A1", "A2", "A3"]
customers = deque(["An", "Khang", "Minh", "Nam", "Sơn", "Tuấn"])

ve_con, khach_con = ban_ve(tickets, customers)
print("Số vé còn lại:", ve_con)
print("Số khách còn lại:", khach_con)    
