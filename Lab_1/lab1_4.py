def fill_bag(w: int, capacity: list):
    """[show what max weight we can bear with inly
        with only one bar of each gold]

    Args:
        w (int): [the weight of the bag where we can put gold bars]
        capacity (list): [all bars of the gold size]
    """

    F = [1] + [0]*w
    for i in range(len(capacity)):
        for j in range(w, capacity[i] - 1, -1):
            if F[j - capacity[i]] == 1:
                F[j] = 1

    i = w
    while F[i] == 0:
        i -= 1
    print(i)


fill_bag(14, [3, 5, 7, 10])
