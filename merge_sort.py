def merge_sort(items, depth=0):
    if len(items) <= 1:
        return items

    indent = "  " * depth
    print(f"{indent}Split {items}")

    mid = len(items) // 2
    left = merge_sort(items[:mid], depth + 1)
    right = merge_sort(items[mid:], depth + 1)

    merged = merge(left, right)
    print(f"{indent}Merge {left} + {right} -> {merged}")
    return merged


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

broken_list =[13,33,7,42,19,28,5]

print (merge_sort(broken_list))