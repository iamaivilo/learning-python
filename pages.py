def pages(a,b):
    if a<b:
        if a%2 == 1 and b%2 == 1: # a odd, b odd
            print(((b-a)/2)+1)
        if a%2 == 1 and b%2 == 0: # a odd, b even
            print((((b+1)-1)/2)+1)
        if a%2 == 0 and b%2 == 1: # a even b odd
            print((((b+1)(a+1))/2)+1)
        if a%2 == 0 and b%2 == 0: # a even, b even
            print(((b-a)/2)+1)
    else:
        print("a>b")

#pages(2,100)

pages(3,11)