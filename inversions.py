def inversions(array):
    result = 0
    length = len(array)

    if length == 1:
        return array, 0
    if length == 2:
        if array[0] <= array[1]:
            return array, 0
        else:
            return [array[1], array[0]], 1
    elif length > 2:
        new_right = length // 2 + 1
        array_left = array[:new_right]
        array_right = array[new_right:]
        array_left, result_left = inversions(array_left)
        array_right, result_right = inversions(array_right)
        array, result_merge = merge(array_left, array_right)
        return array, result_left + result_right + result_merge


def merge(array_left, array_right):
    left, right = 0, 0
    len_left, len_right = len(array_left), len(array_right)
    array_result = []
    inversions_ = 0
    while left < len_left and right < len_right:
        if array_right[right] < array_left[left]:
            array_result.append(array_right[right])
            right += 1
            inversions_ += len_left - left
        else:
            array_result.append(array_left[left])
            left += 1
    while left < len_left:
        array_result.append(array_left[left])
        left += 1
    while right < len_right:
        array_result.append(array_right[right])
        right += 1
    return array_result, inversions_


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    print(inversions(array)[1])
