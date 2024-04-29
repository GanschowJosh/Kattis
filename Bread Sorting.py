def isSortingPossible(breads, desired_order):
    def merge(arr, temp, left, mid, right):
        i = left
        j = mid + 1
        inversions = 0

        for k in range(left, right + 1):
            if i > mid:
                temp[k] = arr[j]
                j += 1
            elif j > right:
                temp[k] = arr[i]
                i += 1
            elif arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                inversions += mid - i + 1

        for k in range(left, right + 1):
            arr[k] = temp[k]

        return inversions

    def mergeSort(arr, temp, left, right):
        inversions = 0
        if left < right:
            mid = (left + right) // 2
            inversions += mergeSort(arr, temp, left, mid)
            inversions += mergeSort(arr, temp, mid + 1, right)
            inversions += merge(arr, temp, left, mid, right)
        return inversions

    temp = [0] * len(breads)
    inversions_breads = mergeSort(breads, temp, 0, len(breads) - 1)
    temp = [0] * len(desired_order)
    inversions_desired = mergeSort(desired_order, temp, 0, len(desired_order) - 1)

    return inversions_breads % 2 == inversions_desired % 2


n = input("")
breads = list(map(int, input().split()))
desired_order = list(map(int, input().split()))

if isSortingPossible(breads, desired_order):
    print("Possible")
else:
    print("Impossible")
