# -------------Question 3: Regression loss -----------------
# import libary
import math
import random


#innitiate variable of later use
loss =[] 

# MAE function:
def mae(num_samples):
  samples =[]
  for i in range(num_samples):
    y_predict = random.uniform(0,10.0)
    y_target = random.uniform(0,10.0)
    loss.append(abs(y_predict-y_target))
    print(f"loss name : MAE , sample : {i} , pred : {y_predict}, target : {y_target} , loss : {loss[i]}")
  final_loss = sum(loss)/num_samples
  return f"final loss : {final_loss}"


# MSE function
def mse(num_samples):
  samples =[]
  for i in range(num_samples):
    y_predict = random.uniform(0,10.0)
    y_target = random.uniform(0,10.0)
    loss.append(abs(y_predict-y_target))
    print(f"loss name : MAE , sample : {i} , pred : {y_predict}, target : {y_target} , loss : {loss[i]}")
  final_loss = sum(loss)/num_samples
  return f"final loss : {final_loss}"

# RMSE function
def rmse(num_samples):
  samples =[]
  for i in range(num_samples):
    y_predict = random.uniform(0,10.0)
    y_target = random.uniform(0,10.0)
    loss.append(abs(y_predict-y_target))
    print(f"loss name : MAE , sample : {i} , pred : {y_predict}, target : {y_target} , loss : {loss[i]}")
  final_loss = math.sqrt(sum(loss)/num_samples)
  return f"final loss : {final_loss}"


# Test output
if __name__ == "__main__":
    
  # input number of samples
  num_samples = input("Input number of samples ( integer number ) which are generated:")

  #check if numeric
  if num_samples.isnumeric():
    num_samples = int(num_samples)

    #input loss name and check if loss name supported
    loss_name = input ("Input loss name(MAE/MSE/RSE)")
    if loss_name == "MAE":
      print(mae(num_samples))
    elif loss_name == "MSE":
      print(mse(num_samples))
    elif loss_name == "RSE":
      print(rmse(num_samples))
    else:
      print("loss name is not supported")
  else:
    print("number of samples must be an integer number")
