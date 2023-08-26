# a good demonstration for functions
def nCr(n,r):
    res=myFactorial(n)/(myFactorial(r)*myFactorial(n-r))
    return res
def myFactorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
        
    return fact
    
print(nCr(10,5))
