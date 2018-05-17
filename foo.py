
print("hello, wolrd")

print("hello, yll")

print("hello, mike")

print("annie, hello")

print("it is 5 lines")

# This is a comment -- 05/15/18
print("Here output the test text; this is coded from Visual Sudio Code -- 05/15/18.")

# Building a python recursive function
def fibo(n):
    if (n <= 1) :
        return(n)
    else:
        return ( fibo(n-1) + fibo(n-2) )

for i in range(10):
    print( 'fibo(%d) = %d' % ( i, fibo(i) ) )
