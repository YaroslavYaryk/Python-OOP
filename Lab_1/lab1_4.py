def fill_bag(w: int, capacity: list):
    """[shows what max weight we can bear 
        with only one bar of each gold]

    Args:
        w (int): [the weight of the bag where we can put gold bars]
        capacity (list): [all bars of the gold size.]
    """

    array = [1] + [0]*w
    for i in range(len(capacity)):
        for j in range(w, capacity[i] - 1, -1):
            if array[j - capacity[i]] == 1:
                array[j] = 1

    i = w
    while array[i] == 0:
        i -= 1
    print(i)


fill_bag(15, [14,5,5,5])
