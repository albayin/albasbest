# Reverse a string
def reverse(text):
  reversed_result = ""
  if len(text) > 1:
    reversed_text = []
    n = len(text)
    while n > 0:
      reversed_text.append(text[n-1])
      n -= 1
      if n == 0:
        break
  	print reversed_text  
    reversed_result = "".join(reversed_text)
  else:
    reversed_result = text
  return reversed_result

print reverse("Hello World!")
