from collections import deque
import math
def radix(nums, base = 10, leftdigit = 0, total_digit = 10):
    # make the buckets
    rightdigit = 10 - leftdigit - 1
    def num_digits(num):
        return int(math.log(num, base)) + 1

    def cal_digit(num, digit):
        return (num // (base ** digit)) % base

    if(len(nums) <= 1):
        return nums
    done_bucket = []
    buckets = [[] for _ in range(base)]
    for num in nums:
        if(leftdigit >= total_digit):
            print(num_digits(num))
            done_bucket.append(num)
        else:
            buckets[cal_digit(num, rightdigit)].append(num)

    #divide and conquer
    buckets = [radix(b, base, leftdigit + 1, total_digit) for b in buckets]
    # extend the list
    return done_bucket + [b for blist in buckets for b in blist]



