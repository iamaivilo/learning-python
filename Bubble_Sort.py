def bubble_sort(numbers):
    n = len(numbers)
    for x in range(n):
        for y in range(0,n-x-1):
            if numbers[y] > numbers[y+1]:
                numbers[y],numbers[y+1] = numbers[y+1],numbers[y]
    return numbers

a = [5,9,2,6,8]
bubble_sort(a)
print("The sorted list is:",a)