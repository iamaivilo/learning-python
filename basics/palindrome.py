def palindromefunc(original): 
    temporary = original
    new_num=0
    while(temporary>0):
        right=temporary%10
        temporary= int(temporary/10)
        new_num=new_num*10+right
    print(new_num)
    return new_num

comparable = 1930391
if (palindromefunc(comparable) == comparable):
    print("This is a palindrome")
else:
    print("this is not a palindrome")