array = [121,5,9,3,7,100,5,8,6,3,2,1]
def merge_sort(list):
    
    length  = len(list)
    if length == 1 :
        return list   
 # divide
    list1 = list[:length//2]
    list2 = list[length//2:]

# recursion
    list3 = merge_sort(list1)
    list4 = merge_sort(list2)
    
    sorted_list = []
    list4_index = 0
    list3_index = 0

#merge 
    while list3_index < len(list1)and list4_index <len(list2):
        if list3[list3_index] > list4[list4_index]:
            sorted_list.append(list4[list4_index])
            list4_index += 1
        else:
            sorted_list.append(list3[list3_index])
            list3_index += 1
    
    if list3_index < len(list3):
        for x in list3[list3_index:]:
            sorted_list.append(x)
    if list4_index < len(list4):
        for x in list4[list4_index:]:
            sorted_list.append(x)
    
    return sorted_list


sorted_list = merge_sort(array)
print(sorted_list)