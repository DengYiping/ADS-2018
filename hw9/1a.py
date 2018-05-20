def h1(k):
    # first hash function
    return k % 5

def h2(k):
    # second hash function
    return (7 * k) % 8

def h(k, i):
    # the double hashing function with size 5
    return (h1(k) + h2(k) * i) % 5

if __name__ == '__main__':
    lst = [3, 10, 2, 4]
    for i in lst:
        print('{} with i = 0 hashes to {}'.format(i, h(i, 0)))

