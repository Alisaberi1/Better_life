def c_range(r,c):
  if c in range(1,11):
    a,b=11-r,c
    return (f"Right {a} {b}")
  elif c not in range(1,11):
    a,b=11-r,21-c
    return (f"Left {a} {b}")
r,c=map(int,input().split(" "))
print(c_range(r,c))