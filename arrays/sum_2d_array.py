def sum_2d_array(array):
    total = 0
    for r in array:
        for e in r:
            total += e
    
    return total

array = [1,2,1], [1,1,2]
print(sum_2d_array(array))
