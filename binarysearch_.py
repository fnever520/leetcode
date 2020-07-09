def bs(arr, first, end, target):
    if first<=end:
        mid = (end - first + first) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return bs(arr, mid+1, end, target)
        
        else:
            return bs(arr, first, mid+1, bs)


def bs(arr, first, end, target):
    while(first<=end):
        mid = (end - first + first) //2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            first = mid +1
        else:
            end = mid + 1
