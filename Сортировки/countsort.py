def countsort(data):
    m = max(data)
    b = [0] * (m + 1)
    for num in data:
        b[num] += 1
    i = 0
    while i < len(data):
        for j in range(len(b)):
            for _ in range(b[j]):
                data[i] = j
                i += 1
    return data
