def count_words_in_file(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        # Đọc toàn bộ nội dung của file và chuyển về chữ thường
        text = file.read().lower()

        # Tách các từ ra (giả sử các từ cách nhau bằng dấu cách)
        words = text.split()
        # Đếm số lần xuất hiện của mỗi từ
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


# Ví dụ sử dụng
file_path = 'Module1-W2/P1_data.txt'  # file path
print(count_words_in_file(file_path))
