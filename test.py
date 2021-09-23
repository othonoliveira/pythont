def max_sum(A):
    max_so_far = 0
    max_ending_here = 0
    min_value=A[0]
    positions=[]
    count=0

    for i in A:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        if max_ending_here != 0:
            positions.append(count)
        max_so_far = max(max_so_far, max_ending_here)
        count+=1

    if A[0] < 0 and A[1] < 0 and A[2] < 0 and A[3] < 0 and A[4] < 0:
        for i in A:
            if i > min_value:
                min_value=i
                positions.append(count)
        return min_value

    else:
        return max_so_far

def position(A):
    max_so_far = 0
    max_ending_here = 0
    min_value=A[0]
    positions=[]
    count=0
    
    for i in A:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        if max_ending_here != 0:
            positions.append(count)
        max_so_far = max(max_so_far, max_ending_here)
        count+=1

    if A[0] < 0 and A[1] < 0 and A[2] < 0 and A[3] < 0 and A[4] < 0:
        for i in A:
            if i > min_value:
                min_value=i
                positions.append(count)
        return positions

    else:
        return positions