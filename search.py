def search(list,target):
    for x in range(len(list)):
        if list[x] == target:
            return x
    return -1


list = [1,45,7,4,8,5,9]
index = search(list,123)
print("the index is:",index)