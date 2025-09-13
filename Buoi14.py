def word_count(text):
    # Chuyển về chữ thường
    text = text.lower()
    # Loại bỏ dấu câu đơn giản
    for ch in ".,!?":
        text = text.replace(ch, "")
    # Tách từ
    words = text.split()

    # Đếm bằng dictionary
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    # In kết quả
    for word, count in freq.items():
        print(word + ":", count)


# ----------------------
# Test


text = "Python is fun. Python is easy to learn."
word_count(text)
