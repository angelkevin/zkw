import math
import copy
import numpy as np
import matplotlib.pyplot as plt
def get_len(x1,x2,y1,y2):
    diff_x = (x1-x2)**2
    diff_y = (y1-y2)**2
    length = np.sqrt(diff_x+diff_y)
    return length
def Srotate(angle,valuex,valuey,pointx,pointy):
  angle = math.radians(angle)
  valuex = np.array(valuex)
  valuey = np.array(valuey)
  sRotatex = (valuex-pointx)*math.cos(angle) + (valuey-pointy)*math.sin(angle) + pointx
  sRotatey = (valuey-pointy)*math.cos(angle) - (valuex-pointx)*math.sin(angle) + pointy
  sRotatex = sRotatex.tolist()
  sRotatey = sRotatey.tolist()
  sRotate = sRotatex + sRotatey
  sRotate = np.array(sRotate)
  return sRotate
def Nrotate(angle,valuex,valuey,pointx,pointy):
  angle = math.radians(angle)
  valuex = np.array(valuex)
  valuey = np.array(valuey)
  nRotatex = (valuex-pointx)*math.cos(angle) - (valuey-pointy)*math.sin(angle) + pointx
  nRotatey = (valuex-pointx)*math.sin(angle) + (valuey-pointy)*math.cos(angle) + pointy
  nRotatex = nRotatex.tolist()
  nRotatey = nRotatey.tolist()
  nRotate = nRotatex + nRotatey
  nRotate = np.array(nRotate)
  return nRotate
def judge(a,b,c,d):
  if min(a[0],b[0])<=max(c[0],d[0]) and min(c[1],d[1])<=max(a[1],b[1]) and min(c[0],d[0])<=max(a[0],b[0]) and min(a[1],b[1])<=max(c[1],d[1]):
    return True
  else:
    return False
 
allBranchs = []
def pltTrees(arr):
  branchLen = get_len(arr[0],arr[1],arr[2],arr[3])
  if branchLen>0.2:
    plt.plot(arr[0:2],arr[2:4])
    arr_next_left = Srotate(20,arr[0:2],arr[2:4],arr[0],arr[2])
    arr_next_left = np.array(arr_next_left)*0.75
    arr_next_left[0:2] = arr_next_left[0:2] - (arr_next_left[0]-arr[1])
    arr_next_left[2:4] = arr_next_left[2:4] - (arr_next_left[2]-arr[3])
    booleanListLeft = []
    for i in range(len(allBranchs)):
      a = [allBranchs[i][0],allBranchs[i][2]]
      b = [allBranchs[i][1],allBranchs[i][3]]
      c = [arr_next_left[0],arr_next_left[2]]
      d = [arr_next_left[1],arr_next_left[3]]
      if a == c or b == d or a == d or b == c:
        continue
      result = judge(a,b,c,d)
      booleanListLeft.append(result)
    if True not in booleanListLeft:
      allBranchs.append(arr_next_left)
      pltTrees(arr_next_left)
    arr_next_right = Nrotate(40,arr_next_left[0:2],arr_next_left[2:4],arr_next_left[0],arr_next_left[2])
    booleanListRight = []
    for i in range(len(allBranchs)):
      a = [allBranchs[i][0],allBranchs[i][2]]
      b = [allBranchs[i][1],allBranchs[i][3]]
      c = [arr_next_right[0],arr_next_right[2]]
      d = [arr_next_right[1],arr_next_right[3]]
      if a == c or b == d or a == d or b == c:
        continue
      result = judge(a,b,c,d)
      booleanListRight.append(result)
    if True not in booleanListRight:
      allBranchs.append(arr_next_right)
      pltTrees(arr_next_right)
  
arr = np.array([1,2,1,2])
pltTrees(arr)
plt.show()
 