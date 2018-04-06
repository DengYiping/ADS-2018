from collections import deque

def find_max_length(words):
    lens = map(len, words)
    return max(lens)

def find_bucket(word, idx):
    if(idx > len(word) - 1):
        # it is out of bound, count it as a very small number
        return 0
    else:
        # return the ascii code
        return ord(word[idx])

def pass_bucket(words, buckets, idx):
    # insert into buckets and pop them out again
    for word in words:
        # First in first out
        buckets[find_bucket(word, idx)].appendleft(word)
    res = []
    # restore the array
    for bucket in buckets:
        while len(bucket):
            res.append(bucket.pop())
    return res


def radix(words):
    # make the buckets
    buckets = [deque() for _ in range(256)]
    max_len = find_max_length(words)
    for idx in reversed(range(max_len)):
        words = pass_bucket(words, buckets, idx)
    return words

if __name__ == "__main__":
    # test case
    words = ["abp", "adp", "awewwss", "aaasdfwe"]
    print("before: {}".format(words))
    print("after: {}".format(radix(words)))

