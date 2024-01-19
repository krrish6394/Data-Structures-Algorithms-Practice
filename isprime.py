def is_prime(a):
    if a == 2:
     return True
    elif a == 1:
     return False
    else:
      count = 0
      for i in range(1, a+1):
          if a % i == 0:
            count+= 1
          else :
            count = count
      print(count)
      if count <= 2 :
            return True
      else :
          return False

print(is_prime(4))

print(is_prime(47))

print(is_prime(45))

print(is_prime(39))

print(is_prime(1))

print(is_prime(2))

