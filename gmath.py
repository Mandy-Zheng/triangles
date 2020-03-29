import math
from display import *

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    length=0
    i=0
    while i<len(vector):
        length+=pow(vector[i],2)
        i+=1
    normal=math.sqrt(length)
    i=0
    while i<len(vector):
        vector[i]=vector[i]/normal
        i+=1
    return vector

#Return the dot porduct of a . b
def dot_product(a, b):
    answer=0
    i=0
    while i<len(a):
        answer+=a[i]*b[i]
        i+=1
    return answer
#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    return None
