# Use String manipulation
def digit_sum_str (x):
  result = 0
  if len(str(x)) >= 2:
    for c in str(x):
      result += int(c)
  else: 
    result = int(x)
  return result

# Use Modulo
def digit_sum_mod (x):
  result = 0
  if x >= 10:
    result += x%10
  else:
    result = x
  return result
