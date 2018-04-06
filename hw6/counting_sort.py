def counting_sort(arr, maximum):
    """Implementing the counting sort algorithm
    """
    countings = [0] * (maximum + 1)
    # initiate a list with zeros
    res = [-1] * len(arr)
    # result
    for entry in arr:
        print("counting of {} is incremented".format(entry))
        countings[entry] = countings[entry] + 1
        # self increment
    print("countings: {}".format(countings))
    print("now we aggregate the countings")
    for idx in range(len(countings) - 1):
        countings[idx + 1] = countings[idx + 1] + countings[idx]
        # aggregate the countings
    print("countings: {}".format(countings))
    print("restore the result")
    for entry in arr:
        # build the result
        # print("entry: {}, count: {}".format(entry, countings[entry]))
        res[countings[entry] - 1] = entry
        print("put {} at index {}".format(entry, countings[entry] - 1))
        countings[entry] = countings[entry] - 1

    return res

if __name__ == "__main__":
    arr = arr = [9, 1, 6, 7, 6, 2, 1]
    print(counting_sort(arr, 9))
