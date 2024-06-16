def max_sliding_window(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    
    result = []
    
    for i in range(n - k + 1):
        current_max = nums[i]
        for j in range(1, k):
            if nums[i + j] > current_max:
                current_max = nums[i + j]
        result.append(current_max)
    
    return result

# Ví dụ sử dụng
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window(num_list, k))