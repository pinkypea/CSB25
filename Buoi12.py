'''1. Lý thuyết:'''
# Khai báo queue
queue = [1, 2, 3]

# Xem phần tử đầu tiên của queue
print(queue[0])

# Thêm phần tử vào queue
queue.append(4)
print(queue)

# Xóa phần tử khỏi queue
front = queue.pop(0)
print(front)
print(queue)

# Kiểm tra queue rỗng
def is_emtpy(queue):
    if len(queue) == 0:
        return True
    else:
        return False
    
'''2. Thực hành:'''
# Bài 1: Cài đặt Queue cơ bản bằng danh sách (list)
# Yêu cầu:
#   - Tạo lớp Queue với các phương thức:
#       + enqueue(item) — thêm phần tử vào cuối hàng đợi.
#       + dequeue() — lấy và xóa phần tử ở đầu hàng đợi.
#       + is_empty() — kiểm tra hàng đợi có rỗng không.
#       + size() — trả về số lượng phần tử trong hàng đợi.
# Thử sử dụng hàng đợi để lưu và lấy các số nguyên từ 1 đến 5.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)
        
q = Queue()
for i in range (1, 6):
    q.enqueue(i)

while not q.is_empty():
    print(q.dequeue())


# Bài 2: Mô phỏng hệ thống xếp hàng
# Yêu cầu:
#   - Người dùng đến quầy giao dịch và lấy số thứ tự từ 1 đến 5.
#   - Mỗi lượt xử lý, quầy giao dịch lấy số tiếp theo trong hàng đợi và thông báo "Đang phục vụ khách hàng số X".
#   - In ra danh sách còn lại trong hàng đợi sau mỗi lượt.
#   - Gợi ý: Có thể dùng collections.deque để tối ưu:

# enqueue các số từ 1 đến 5
# xử lý đến khi hàng đợi rỗng

queue1 = []
for i in range(1, 6):
    queue1.append(i)

def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False
    
while not is_empty(queue1):
    current = queue1.pop(0)
    print(f"Đang phục vụ khách hàng thứ {current}")
    print(f"Hàng chờ còn {len(queue1)} khách hàng")

from collections import deque
queue1 = deque()

for i in range(1, 6):
    queue1.append(i)

def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False
    
while not is_empty(queue1):
    current = queue1.popleft()
    print(f"Đang phục vụ khách hàng thứ {current}")
    print(f"Hàng chờ còn {len(queue1)} khách hàng")

# Lập trình ứng dụng MP3Player

import queue
class MP3Player:
    def __init__(self):
        self.music_queue = queue.Queue()
        self.current_song = None

    def add_song(self, song):
        self.music_queue.put(song)

    def play_next_song(self):
        if self.music_queue.empty():
            print("Hàng đợi không có bài hát nào đang chờ")
        else:
            self.current_song = self.music_queue.get()
            print(f"Chơi bài hát {self.current_song}")

    def skip_song(self):
        if self.current_song is None:
            print("Không thể bỏ qua do không có bài hát nào đang được chạy")
        else:
            self.current_song = None
            self.play_next_song()
