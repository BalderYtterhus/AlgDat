# Find largest element in unimodal list
# Example of unimodal list: [1, 3, 5, 6, 4, 2]
# Use ideas from binary search:
    # Find length check compare two middle elements and go in the direction of the larger one
    # Loop untill you either hit the wall or find a smaller one

def find_maximum(x):
    lo, hi = 0, len(x) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if x[lo] < x[hi]:
            if x[mid] > x[mid + 1] and x[mid] > x[hi]:
                hi = mid
            else:
                lo = mid + 1
        else:
            if x[mid] < x[mid + 1] and x[mid + 1] > x[lo]:
                lo = mid + 1 
            else:
                hi = mid

    return x[lo]
    







    
