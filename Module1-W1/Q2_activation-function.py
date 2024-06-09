# -------------Question 1: Activation function -----------------
# import libary
import math

# function check is number
def is_number(x):
  try :
    float (x) 
  except ValueError :
    return False
  return True

# Sigmoid formular
def sigmoid(x):
    result = 1/(1 + math.exp(-x))
    return result

# Relu formular
def relu(x):
    result = max(0, x)
    return result

# Elu formular
def elu(x, alpha = 0.01):
    if x > 0:
        result = x
    else:
        result = alpha * (math.exp(x) - 1)
    return result


# Activate Function, take 2 arg, number x and type of function
def activate_function(x, function):
    if function == "sigmoid":
        return sigmoid(x)
    elif function == "relu":
        return relu(x)
    elif function == "elu":
        return elu(x, alpha = 0.01)
    else:
        return print (function + ' is not supported')

# Runing the activate function
# User input for number x and choose which function to use
x = input("Enter a value: ")
if is_number(x):
    x = float(x)
    function = input("Enter a function (sigmoid, relu, elu): ")
    print(activate_function(x, function))
else:
    print("x must be a number")


