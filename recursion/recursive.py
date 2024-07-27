

# def recursiveMethod(n):
#   if n < 1:
#     print("n is less then 1")
#   else:
#     recursiveMethod(n-1)
#     print(n)


# recursiveMethod(46)



def recursiveMethod2(m):
  if m == 0 :
    print("Num less then 1")
  else:
    power = recursiveMethod2(m-1)
    return power * 2

n = recursiveMethod2(44)
print(n)
