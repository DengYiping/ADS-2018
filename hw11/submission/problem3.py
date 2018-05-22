
def picking_order(adj_matrix):
    rst = [] #storing the result
    
    for i in range(len(adj_matrix)):
        pos = 0
        for w in rst:
            if not adj_matrix[w][i]:
                break
            pos = pos + 1
        rst = rst[0:pos] + [i] + rst[pos:]
    return rst

