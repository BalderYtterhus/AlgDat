def longest_decreasing_subsequence(s:list)->list:
    if len(s) == 0:
        return []
    
    lcs_len = [1]*(len(s))
    # A = [7, 4, 6, 3]
    # l = [1, 2, 2, 3]

    for i in range(1, len(s)):
        for j in range(i):
            if s[j] > s[i]:
                lcs_len[i] = max(lcs_len[i], lcs_len[j] + 1)

    length = max(lcs_len)

    index = 0
    for i in range(len(s)):
        if lcs_len[i] == length:
            index = i
        else:
            continue

    res = [s[index]]
    i = 1

    while len(res) != length:
        if s[index - i] > s[index]:
            res.insert(0, s[index - i])
            i += 1

    return res


