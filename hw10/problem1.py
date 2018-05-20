# Yiping Deng
def main_func():
    # main function to take the input
    
    # take the input
    inp = list(map(int, input().split())) #convert it into list

    rst = longestOrderedSubarray(inp)

    print(*rst, sep=' ')

def longestOrderedSubarray(arr):
    """
    Calculate the longest subarray
    >>> longestOrderedSubarray([8,3,6,50,10,8,100,30,60,40,80])
    [3, 6, 10, 30, 60, 80]
    """
    cache = {} #memoization
    def helper(start, previous):
        """
        Calculate the longest ordered subarray.
        arr: list of integers
        start: index of the start of the array
        end: index of the end of the array
        previous: the biggest element in the previous subarray

        return the array
        """
        nonlocal cache

        if start >= len(arr):
            return []

        # if not yet computed
        if (start, previous) not in cache:

            # if you cannot take this element
            if arr[start] < previous:
                cache[(start, previous)] = helper(start + 1, previous)
            else:
                # if you can take it, find the best case
                inclusive = helper(start + 1, arr[start])
                exclusive = helper(start + 1, previous)

                # consider two cases, and decide the best case
                if (len(inclusive) + 1) >= len(exclusive):
                    cache[(start, previous)] = [arr[start]] + inclusive
                else:
                    cache[(start, previous)] =  exclusive

        return cache[(start, previous)]

    # call the helper function
    # use -infinity so that you can always take the first
    # one
    return helper(0, float('-inf'))

if __name__ == '__main__':
    main_func()
