def binary_search(arr: list[int], value: int) -> int:
    start: int = 0
    end: int = len(arr) - 1

    while start <= end:
        mid: int = (start + end) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

if __name__ == '__main__':
    arr: list[int] = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    val: int = 23

    search: int = binary_search(arr, val)

    if search != -1:
        print(f'Valor {val} en index: {search}')
    else:
        print(f'Valor {val} no encontrado en la lista')