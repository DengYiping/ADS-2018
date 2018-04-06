def insertion_sort(lst):
    """ Implementation of insertion sort in python
    >>> insertion_sort([4, 3, 2 ,1])
    [1, 2, 3, 4]
    """
    print("calling the insertion sort on {}".format(lst))
    for idx in range(1, len(lst)):
        val = lst[idx] # current value
        pos = idx # current position

        # move the element
        while pos > 0 and lst[pos -1] > val:
            lst[pos] = lst[pos - 1]
            pos = pos - 1

        lst[pos] = val

    return lst

def bucket_sort(arr):
    maximum = 1.0
    minimum = 0.0
    num_bucket = len(arr)
    step = (maximum - minimum) / float(num_bucket)
    print("number of bucket: {}".format(num_bucket))
    buckets = [[] for _ in range(num_bucket)]
    print(buckets)
    print("build empty buckets")

    def find_bucket(i):
        print("find bucket for {}".format(i))
        return int(i / step)

    res = []

    print("start to put in buckets")
    for entry in arr:
        b = find_bucket(entry)
        print("put in bucket {}".format(b))
        buckets[b].append(entry)
        print("now in buckets we have {}".format(buckets))

    for bucket in buckets:
        n_bkt = insertion_sort(bucket)
        res = res + n_bkt
        print("building results by adding {}".format(n_bkt))

    return res

if __name__ == "__main__":
    arr = [0.9, 0.1, 0.6, 0.7, 0.6, 0.2, 0.1]
    print(bucket_sort(arr))
