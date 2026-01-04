def q0_pythagoras(m,n) : 
    x = m** 2 + n**2 
    return x**0.5

def q1_is_pythagoras(a,b,c):
    while a > b and  a > c :
         if a**2 == b**2 + c**2 :
            return True 
         else : return False 
    while b > a and b > c :
          if b**2 == a**2 + c**2 :
            return True 
          else : return False 
    while c > a and c > b :
          if c**2 == b**2 + a**2 :
             return True 
          else : return False 

def q2_get_last_index(a,n):
    for i in range (len(a)-1,-1,-1):
        if a[i] == n :
            return i 
    return -1 

