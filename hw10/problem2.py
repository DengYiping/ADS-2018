def main_func():
    inp = []

    while True:
        # continously taking input
        inp_line = list(map(int, input().split()))
        if len(inp_line) == 0:
            break
        inp.append(inp_line)

    #calculate the result
    total_sum, path = decideroad(inp)

    #print the result
    print(total_sum)
    print(*path, sep = ' ')

def decideroad(arr):
    cache = {}
    def helper(level, position):
        # helper function decide road at different level
        nonlocal cache
        if level >= len(arr):
            # out of bound
            return []
        if (level, position) not in cache:
            if level == 0:
                cache[(level, position)] = [arr[level][position]] + helper(1, 0)
            else:
                left = [arr[level][position]] + helper(level + 1, position)
                right = [arr[level][position]] + helper(level + 1, position + 1)

                leftSum = sum(left)
                rightSum = sum(right)

                if leftSum >= rightSum:
                    cache[(level, position)] = left
                else:
                    cache[(level, position)] = right
        return cache[(level, position)]
    rst = helper(0,0)
    return sum(rst), rst

if __name__ == '__main__':
    main_func()
