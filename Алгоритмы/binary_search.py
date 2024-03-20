# Левый бинарный поиск (lbs)
def lbs(a, x):
    left = -1
    right = len(a) - 1
    while left + 1 != right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid
        else:
            right = mid
    return right


# Правый бинарный поиск (rbs)
def rbs(a, x):
    left = 0
    right = len(a)
    while left + 1 != right:
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid
        else:
            left = mid
    return left
