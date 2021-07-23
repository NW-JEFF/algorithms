"""Divide-and-conquer method."""


def find_max_crossing_subarray(a, low, mid, high):
    """Find maximum crossing subarray in O(n) time complexity.

    Parameters
    ----------
    a : array
        The full array used.
    low : int
        The starting index of the subarray we concern here based on `a`.
    mid : int
        The middle index of the subarray we concern here based on `a`.
    high : int
        The ending index of the subarray we concern here based on `a`.

    Returns
    -------
    i : int
        Starting index of max crossing subarray.
    j : int
        Ending index of max crossing subarray.
    sum : float
        sum of max crossing subarray.
    """
    l_record = -float("inf")
    l_sum = 0
    for k in range(mid, low-1, -1):
        l_sum += a[k]
        if l_sum > l_record:
            l_record = l_sum
            i = k
    r_record = -float("inf")
    r_sum = 0
    for k in range(mid+1, high+1):
        r_sum += a[k]
        if r_sum > r_record:
            r_record = r_sum
            j = k
    return (i, j, l_record+r_record)


def find_max_subarray(a, low, high):
    """Find maximum crossing subarray in O(nlgn) time complexity."""
    if low == high:  # base case
        return (low, high, a[low])
    else:  # divide-and-conquer, break into 2 subarrays
        mid = (high+low)//2
        l_low, l_high, l_sum = find_max_subarray(a, low, mid)
        r_low, r_high, r_sum = find_max_subarray(a, mid+1, high)
        m_low, m_high, m_sum = find_max_crossing_subarray(a, low, mid, high)
        if l_sum >= r_sum and l_sum >= m_sum:
            return (l_low, l_high, l_sum)
        elif r_sum >= l_sum and r_sum >= m_sum:
            return (r_low, r_high, r_sum)
        else:
            return (m_low, m_high, m_sum)
