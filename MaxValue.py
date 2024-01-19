def max_value(abc):
  cde = abc[0]
  if len(abc)<=1 :
    return abc[0]
  d =  len(abc)
  for i in range(0, d):
   if abc[i] > cde:
    cde = abc[i] 
   else:
    cde = cde
  return cde

 
a = max_value([4, 7, 2, 8, 10, 9]) 

print (a)

b = max_value([10, 5, 40, 40.3]) 

print (b)

c = max_value([-5, -2, -1, -11]) 

print (c)
d = max_value([42]) 

print (d)
e = max_value([2, 5, 1, 1, 4]) 

print (e)
f = max_value([1000, 8, 9000]) 

print (f)