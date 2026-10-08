def flexradix(A: list, n: int, d: int) -> list:
    if not A:
        return []

    max_len = 0
    for word in A:
        if len(word) > max_len:
            max_len = len(word)

    B = [[] for _ in range(max_len + 1)]

    for word in A:
        B[len(word)].append(word)

    aktiv = []
    a_ord = ord('a')

    for i in range(max_len - 1, -1, -1):
        aktiv = B[i + 1] + aktiv

        buckets = [[] for _ in range(26)]

        for navn in aktiv:
            buckets[ord(navn[i]) - a_ord].append(navn)

        aktiv = []
        for bucket in buckets:
            aktiv.extend(bucket)

    return aktiv