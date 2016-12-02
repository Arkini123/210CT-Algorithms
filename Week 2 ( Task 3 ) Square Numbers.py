def square_number(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1

        if ans*ans != x:  
            print (x, 'This is not a perfect square number.')
            return None
        else:
            print (x, ' This is a perfect sqaure number.')
            return ans


y = int(input("Enter a number"))
print(square_number(y))

import timeit

start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print (stop - start) 
