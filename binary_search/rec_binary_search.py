def recursive_binary_search(arr: list[int], low: int, high: int, val: int) -> int:
    if low > high:
        return -1

    mid: int = (low + high) // 2

    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        return recursive_binary_search(arr, low, mid - 1, val)
    else:
        return recursive_binary_search(arr, mid + 1, high, val)

if __name__ == '__main__':
    arr: list[int] = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    val: int = 5

    search: int = recursive_binary_search(arr, 0, len(arr) - 1, val)

    if search != -1:
        print(f'Valor {val} en index: {search}')
    else:
        print(f'Valor {val} no encontrado en la lista')