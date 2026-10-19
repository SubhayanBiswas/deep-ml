def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
                  import numpy as np
                  a = np.array(a)
                  b = np.array(b)
                  p1 = a.shape[1]
                  p2 = b.shape[0]
                  if p1 == p2:
                      c = np.dot(a, b)
                  else:
                      c = -1
                  return c