# give you a list [9,10,38,81,100,7,1], there's no repeated numbers in the list. 
# please define a function find_max(list),  find the max number in the list and output it

def max_list(list):
    MIN_INT_64 = -9_223_372_036_854_775_808
    output = MIN_INT_64
    for x in list:
        if x > output:
            output = x
    print(output)

# from olivia
def second_largest(list,max):
    max_int=9_223_372_036_854_775_808
    for x in list:
        if max - x != 0:
            if max - x < max_int:
                max_int=max-x
    print(max-max_int)

# from shane
def second_max_list(list):
    MIN_INT_64 = -9_223_372_036_854_775_808
    first_largest = MIN_INT_64
    second_largest = MIN_INT_64
    if len(list) <= 1:
        print("no second number can not find result")
        return
    for x in list:
        if x > second_largest and x < first_largest:
            second_largest = x
        if x > first_largest:
            second_largest = first_largest
            first_largest = x
    print(second_largest)


second_largest([9,10,38,81,100,7,1], max_list([9,10,38,81,100,7,1]))