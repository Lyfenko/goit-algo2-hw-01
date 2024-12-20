def find_min_max(arr):
    n = len(arr)
    if n == 0:
        return (None, None)
    if n == 1:
        return (arr[0], arr[0])
    if n == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    mid = n // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)

    return (minimum, maximum)


arr = [3, 5, 1, 9, 2, 7, 4, 8, 6]
min_val, max_val = find_min_max(arr)
print(f"Мінімум: {min_val}, Максимум: {max_val}")

arr_empty = []
min_val_empty, max_val_empty = find_min_max(arr_empty)
print(
    f"Мінімум (порожній масив): {min_val_empty}, Максимум (порожній масив): {max_val_empty}"
)

arr_single = [5]
min_val_single, max_val_single = find_min_max(arr_single)
print(
    f"Мінімум (один елемент): {min_val_single}, Максимум (один елемент): {max_val_single}"
)
