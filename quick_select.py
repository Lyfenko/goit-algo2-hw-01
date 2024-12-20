import random


def quick_select(arr, k):

    if not arr or k <= 0 or k > len(arr):
        return None

    def _quick_select(arr, left, right, k):
        if left == right:
            return arr[left]

        pivot_index = random.randint(left, right)
        pivot = arr[pivot_index]

        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[right], arr[store_index] = arr[store_index], arr[right]

        if k == store_index + 1:
            return pivot
        elif k < store_index + 1:
            return _quick_select(arr, left, store_index - 1, k)
        else:
            return _quick_select(arr, store_index + 1, right, k)

    return _quick_select(arr, 0, len(arr) - 1, k)


arr = [3, 5, 1, 9, 2, 7, 4, 8, 6]
k = 3
kth_smallest = quick_select(arr, k)
print(f"{k}-й найменший елемент: {kth_smallest}")

arr_empty = []
kth_smallest_empty = quick_select(arr_empty, k)
print(f"{k}-й найменший елемент (порожній масив): {kth_smallest_empty}")

arr_single = [5]
kth_smallest_single = quick_select(arr_single, 1)
print(f"1-й найменший елемент (один елемент): {kth_smallest_single}")