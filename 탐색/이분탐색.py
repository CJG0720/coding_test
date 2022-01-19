n = 10
target = 13
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search(array, target, 0, n-1)
if result == None:
    print(None)
else:
    print(str(result+1) + '번째에 있음')