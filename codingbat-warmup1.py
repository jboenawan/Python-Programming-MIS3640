#sleep_in 
def sleep_in(weekday, vacation):
  if vacation:
    return True
  elif weekday:
    return False
  else: 
    return True

#monkey_trouble 
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True 
  elif not a_smile and not b_smile:
    return True
  else: 
    return False

#sum_double 
def sum_double(a, b):
  sum = a+b
  if a == b:
    return sum*2
  else:
    return sum

#diff21
def diff21(n):
  n = int(n)
  diff = abs(n - 21)
  if n > 21: 
    return diff*2
  elif n <=21:
    return diff
    
#parrot_trouble 
def parrot_trouble(talking, hour):
  if talking and (hour <7 or hour >20):
    return True 
  else:
    return False

#near_hundred 
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#pos_neg
def pos_neg(a, b, negative):
  if negative: 
    if a < 0 and b < 0:
      return True 
    else: 
      return False 
  elif (a < 0 and b > 0) or (a > 0 and b < 0):
    return True 
  else: 
    return False 

#not_string 
def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str

#missing_char
def missing_char(str, n):
  return str[:n] + str[n+1:]

#front_back 
def front_back(str):
  if len(str) <=1:
    return str
  mid = str[1:len(str)-1]
  return str[len(str)-1] + mid + str[0]

#front3
def front3(str):
  return str[:3] + str[:3] +str[:3]

