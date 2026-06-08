while True:
  line = input().strip()
  if line == "END":
    break
  if line == "1":
    print(1)
    continue
  
  curr = len(line)  # Current number of digits
  i = 2  # Start from the second iteration
  
  while True:
    next_digits = 0
    temp = curr
    
    # Count the number of digits in curr
    while temp > 0:
      temp //= 10
      next_digits += 1
    
    if curr == next_digits:
      print(i)
      break
    
    i += 1
    curr = next_digits  # Update curr for the next iteration
