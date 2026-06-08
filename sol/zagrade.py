expression = input().strip()
char_list = list(expression)

valid_combinations = set()

opening_indices = []
closing_indices = []

for i, char in enumerate(char_list):
  if char == '(':
    opening_indices.append(i)
  elif char == ')':
    if opening_indices:
      opening_index = opening_indices.pop()
      closing_indices.append((opening_index, i))

for mask in range(1, 1 << len(closing_indices)):
  selected_indices = []

  for i in range(len(closing_indices)):
    if mask & (1 << i):
      selected_indices.append(i)

  modified_chars = char_list[:]
  for i in selected_indices:
    modified_chars[closing_indices[i][0]] = ''
    modified_chars[closing_indices[i][1]] = ''

  valid_combinations.add(''.join(modified_chars))

for combination in sorted(valid_combinations):
  print(combination)
