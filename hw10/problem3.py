def main_func():
    # do some reading and execute the strategy
    num_cases = int(input()) # take the input

    inputs = []
    for _ in range(num_cases):

        target_line = input().split()

        oxygen = int(target_line[0])
        nitrogen = int(target_line[1])

        num_cylinders = int(input())

        cylinders = []

        for _ in range(num_cylinders):
            cylinder_line = input().split()

            cylinder_oxy = int(cylinder_line[0])
            cylinder_nitro = int(cylinder_line[1])
            cylinder_weight = int(cylinder_line[2])

            cylinders.append((cylinder_oxy, cylinder_nitro, cylinder_weight))

        inputs.append((oxygen, nitrogen, cylinders))

    # start solving the case
    results = map(lambda tup: scubaSolve(tup[2], tup[0], tup[1]), inputs)

    for result_total, result_cylinders in results:
        print(result_total)
        one_indexed = map(lambda x: x + 1, result_cylinders)
        print(*one_indexed, sep = ' ')


def scubaSolve(cylinders, oxygen, nitrogen):
    # such cache is actually 3 dimension, so let it be
    cache = {} # dynamic programming

    def helper(idx, oxygen, nitrogen):
        nonlocal cache # access the dynamic programming cache

        if oxygen <= 0 and nitrogen <= 0: 
            # solution reached, return 0 and empty list
            return 0, []

        if idx >= len(cylinders):
            # no solution given
            return None

        if (idx, oxygen, nitrogen) not in cache:
            cylinder_oxy, cylinder_nitro, cylinder_weight = cylinders[idx]

            # break into two cases
            # included is guaratee to have solution
            included = helper(idx + 1, oxygen - cylinder_oxy, nitrogen - cylinder_nitro)

            if included is None:
                # if not solvable
                cache[(idx, oxygen, nitrogen)] = None
            else:
                # default optimal
                excluded = helper(idx + 1, oxygen, nitrogen)

                optimal_total, optimal_cylinders = included
                optimal_total, optimal_cylinders = optimal_total + cylinder_weight, [idx] + optimal_cylinders

                if excluded is not None:
                    # find the optimal solution
                    excluded_total, excluded_cylinders = excluded
                    if optimal_total > excluded_total:
                        optimal_total, optimal_cylinders = excluded_total, excluded_cylinders

                # put it into the cache
                cache[(idx, oxygen, nitrogen)] = optimal_total, optimal_cylinders

        return cache[(idx, oxygen, nitrogen)]

    return helper(0, oxygen, nitrogen)

if __name__ == '__main__':
    main_func()
