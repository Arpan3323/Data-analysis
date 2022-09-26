import numpy as np

# a method to convert a list into a 3x3 matrix and calculate mean, variance, standard deviation, max, min, 
# and sum along both axes and for the flattened matrix

def calculate(list):
  if (len(list)<9):
    raise ValueError("List must contain nine numbers.")
  A = np.array(list).reshape(3,3)
  mean1 = (A.mean(axis = 0)).tolist()
  mean2 = (A.mean(axis = 1)).tolist()
  mean3 = (A.flatten().mean()).tolist()
  variance1 = (A.var(axis=0)).tolist()
  variance2 = (A.var(axis=1)).tolist()
  variance3 = (A.flatten().var()).tolist()
  std1 = (A.std(axis=0)).tolist()
  std2 = (A.std(axis=1)).tolist()
  std3 = (A.flatten().std()).tolist()
  max1 = (A.max(axis=0)).tolist()
  max2 = (A.max(axis=1)).tolist()
  max3 = (A.flatten().max()).tolist()
  min1 = (A.min(axis=0)).tolist()
  min2 = (A.min(axis=1)).tolist()
  min3 = (A.flatten().min()).tolist()
  sum1 = (A.sum(axis = 0)).tolist()
  sum2 = (A.sum(axis = 1)).tolist()
  sum3 = (A.flatten().sum()).tolist()
  
  #returning the result in a dictionary
  
  calculations = {'mean': [mean1, mean2, mean3],
  'variance': [variance1, variance2, variance3],
  'standard deviation': [std1, std2, std3],
  'max': [max1, max2, max3],
  'min': [min1, min2, min3],
  'sum': [sum1, sum2, sum3]}


  
  return calculations
