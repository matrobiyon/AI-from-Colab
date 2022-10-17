def fibonachi(a):
  if a >= 3:
    fib1,fib2 = 1,1
    print(fib1,fib2,end=" ")
    for i in range(3,a):
      print(fib2+fib1, end=" ")
      fib1,fib2 = fib2, fib1+fib1
  else:
    print("Wrong number")