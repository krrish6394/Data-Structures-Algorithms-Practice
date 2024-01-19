# uncompress
# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

# <number><char>

# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(s):
  numb='0123456789'
  res=[]
  i=0
  j=0
  while j < len(s):
     if  s[j] in numb:
        j+=1
        
     else:
        num=int(s[i:j])
        # res.append(s[j]*num)
        res.append(s[j]*num)
        j+=1
        i=j
        
  return ''.join(res)

print("Solution of 2c3a1t is "+ uncompress("2c3a1t"))
print("Solution of 4s2b is "+ uncompress("4s2b"))
print("Solution of 3n12e2z is "+ uncompress("3n12e2z"))
print("Solution of 2p1o5p is "+ uncompress("2p1o5p"))
print("Solution of 2c4s3x1g is "+ uncompress("2c4s3x1g"))



