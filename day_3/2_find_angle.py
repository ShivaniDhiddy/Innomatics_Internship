import math

ab= int(input())
bc = int(input())
hypo= (math.sqrt(ab**2 + bc**2))/2
adj = bc/2
theta= int(round(math.degrees(math.acos(adj/hypo))))
print(str(theta)+"°")
