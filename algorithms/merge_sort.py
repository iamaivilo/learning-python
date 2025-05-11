def merge_sort(list):
    length = len(list)
    if length == 1:
        return list    
    left = list[:length//2]
    right = list[length//2:]
    s_left = merge_sort(left)
    s_right = merge_sort(right)
    left_index = 0
    right_index = 0
    final_list = []
    while left_index < len(left) and right_index < len(right):
        if s_left[left_index] > s_right[right_index]:
            final_list.append(s_right[right_index])
            right_index += 1
        else:
            final_list.append(s_left[left_index])
            left_index += 1
    if left_index < len(left) :
        for x in s_left[left_index:]:
            final_list.append(x)
    if right_index < len(right) :
        for y in s_right[right_index:]:
            final_list.append(y)
    return final_list
    


list = [6,4,7,7,76,4,98,9,2,5,3,7,3]
x = merge_sort(list)
print("The sorted list is",x)