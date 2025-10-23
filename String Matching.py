# def loop(string, pattern):
#   l = len(pattern)
#   # print("L:",l)
#   for i in range(len(string) - l + 1):
#     # print("curr string: ",string[i:i+l])
#     if string[i:i+l] == pattern:
#       print(i, end=" ")
#   print()

def kmp_search(text, pattern):
  n, m = len(text), len(pattern)
  lps = [0]*m
  
  j = 0
  for i in range(1, m):
    while j > 0 and pattern[i] != pattern[j]:
      j = lps[j-1]
    if pattern[i] == pattern[j]:
      j += 1
      lps[i] = j
  
  j = 0
  for i in range(n):
    while j > 0 and text[i] != pattern[j]:
      j = lps[j-1]
    if text[i] == pattern[j]:
      j += 1
      if j == m:
        print(i-m+1, end=" ")
        j = lps[j-1]
  print()

while True:
  try:
    patt = input()
    string = input()
    kmp_search(string, patt)
    # for i in loop(string, patt):
    #   print(i)
  except:
    break