def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by the start times
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:  # Overlap
            prev[1] = max(prev[1], current[1])  # Merge
        else:
            merged.append(current)

    return merged

# Test
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
