def merge_intervals(intervals):
    # Empty list check
    if not intervals:
        return []
    
    # Step 1: sort pannuvom -> starting value base la
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]  # first interval add pannuvom
    
    for current in intervals[1:]:
        last = merged[-1]   # already merged last interval
        if current[0] <= last[1]:  
            # overlap iruku -> merge pannuvom
            last[1] = max(last[1], current[1])
        else:
            # overlap illa -> direct append
            merged.append(current)
    
    return merged

