def res(A):
    max_so_far = 0
    max_ending_here = 0
    sum_negative=0
    min_value=0
    positions=[]
    count=0
    for i in A:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)
        if i < min_value:
            min_value=i
    
    if max_so_far >= 0:
        for i in A:
            

    if min_value<0:
        for i in A:
            if i > min_value:
                min_value=i
                positions.append(count)

        return min_value , positions

    return max_so_far

r=[1,2,3,4,-1000]
print(res(r))