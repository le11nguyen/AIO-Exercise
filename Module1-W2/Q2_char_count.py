def count_chars(string):
    char_count = {}
    for char in string:
        # Đếm số lần xuất hiện của mỗi từ
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Ví dụ sử dụng
string1 = "Happiness"
print(count_chars(string1))

string2 = "smiles"
print(count_chars(string2))