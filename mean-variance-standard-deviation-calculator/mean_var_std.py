import numpy as np

def calculate(list):
  try:
    m = np.array(list).reshape(3,3)
  except ValueError:
    raise ValueError("List must contain nine numbers.")
  calculations = {}
  b1=[np.mean(m,axis=0).tolist(),np.mean(m,axis=1).tolist(),np.mean(m)]
  b2=[np.var(m,axis=0).tolist(),np.var(m,axis=1).tolist(),np.var(m)]
  b3=[np.std(m,axis=0).tolist(),np.std(m,axis=1).tolist(),np.std(m)]
  b4=[np.max(m,axis=0).tolist(),np.max(m,axis=1).tolist(),np.max(m)]
  b5=[np.min(m,axis=0).tolist(),np.min(m,axis=1).tolist(),np.min(m)]
  b6=[np.sum(m,axis=0).tolist(),np.sum(m,axis=1).tolist(),np.sum(m)]    
  
  calculations = {'mean':b1, 'variance':b2, 'standard deviation':b3, 'max':b4,'min':b5,'sum':b6}
  return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))