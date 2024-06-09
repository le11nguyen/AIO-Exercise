# -------------Question 4: Estimate -----------------

import math

#factorial funciton
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#Estimate sin function
def sin_estimate(x=3.14, n=10):
  if n < 1:
    return "n must be greater than 1"
  result = 0
  for i in range(n):
    result += ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
  return result
print(sin_estimate(x=3.14, n=10))


#estimate cosin function
def cos_estimate(x=3.14, n=10):
  if n < 1:
    return "n must be greater than 1"
  result = 0
  for i in range(n):
    result += ((-1)**i)*(x**(2*i))/factorial(2*i)
  return result
print(cos_estimate(x=3.14, n=10))


#Estimate sinh function
def sinh_estimate(x=3.14, n=10):
  if n < 1:
    return "n must be greater than 1"
  result = 0
  for i in range(n):
    result += ((x**(2*i+1))/factorial(2*i+1))
  return result
print(sinh_estimate(x=3.14, n=10))

#estimate cosh function
def cosh_estimate(x=3.14, n=10):
  if n < 1:
    return "n must be greater than 1"
  result = 0
  for i in range(n):
    result += ((x**(2*i))/factorial(2*i))
  return result
print(cosh_estimate(x=3.14, n=10))