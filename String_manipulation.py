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

# Remove Vowels

def anti_vowel(text):
  vowels = "aeiouAEIOU"
  result = text
  for c in result:
    print c
    if vowels.find(c) != -1:
      print "found it"
      result = result.replace(c,"")
    else:
      print "no vowel found"
  return result

# Find string and replace them with *
def censor(text, word):
  result = text
  temp = word
  while result.find(word) != -1:
    for c in word:
      temp = temp.replace(c, "*")
    result = result.replace(word, temp)
  else:
    print "no word found to be censored."
  
  print result
  return result
