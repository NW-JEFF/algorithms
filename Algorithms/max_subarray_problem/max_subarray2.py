"""O(n) time complexity method."""


def find_max_subarray(arr):
    """Find max subarray in O(n) time complexity."""
    # base case
    i = 0  # begining and ending indeces of max sub array
    j = 0
    sum = arr[0]
    n = 0  # starting index of the max subarray with rightmost end
    sum2 = arr[0]
    for k in range(1, len(arr)):
        if sum2 >= 0:  # arr[k]+sum2 is larger than arr[k]
            sum2 += arr[k]
        else:
            sum2 = arr[k]
            n = k
        if sum2 > sum:
            i = n
            j = k
            sum = sum2
    return (i, j, sum)
