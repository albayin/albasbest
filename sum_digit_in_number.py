# Use String manipulation
def digit_sum_str (x):
  result = 0
  if len(str(x)) >= 2:
    for c in str(x):
      result += int(c)
  else: 
    result = int(x)
  return result

# Use Modulo and Floor division
def digit_sum (x):
  if x >= 10:
    result = x%10
    temp = x//10
    while temp > 9:
      result += temp%10
      print result
      temp = temp // 10
      if temp < 10: 
        result += temp
        break
    else:
      result = temp + x%10
  else:
    result = x
  return result

#test result
print digit_sum (89) 
