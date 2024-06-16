def levenshtein_distance(source, target):
    # Tạo ma trận lưu trữ
    m, n = len(source), len(target)
    D = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Khởi tạo hàng và cột đầu tiên
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    # Tính toán các giá trị trong ma trận
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            D[i][j] = min(D[i - 1][j] + 1,    # Chi phí xoá
                          D[i][j - 1] + 1,    # Chi phí thêm
                          D[i - 1][j - 1] + cost)  # Chi phí thay thế

    # Giá trị tại ô cuối cùng là khoảng cách Levenshtein
    return D[m][n]

source = "hola"
target = "hello"
print(levenshtein_distance(source, target))