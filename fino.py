def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a number greater than 0: ")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))