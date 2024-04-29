# Get the input expression as a string and convert it into a list of characters
expression = input().strip()
char_list = list(expression)

# Initialize a set to store unique valid combinations
valid_combinations = set()

# Initialize lists to store opening and closing parenthesis indices
opening_indices = []
closing_indices = []

# Find pairs of matching parentheses and store their indices
for i, char in enumerate(char_list):
    if char == '(':
        opening_indices.append(i)
    elif char == ')':
        if opening_indices:
            opening_index = opening_indices.pop()
            closing_indices.append((opening_index, i))

# Generate all possible combinations of matching parentheses
for mask in range(1, 1 << len(closing_indices)):
    selected_indices = []

    # Determine which pairs of parentheses are selected for this combination
    for i in range(len(closing_indices)):
        if mask & (1 << i):
            selected_indices.append(i)

    # Create a copy of the character list with selected parentheses removed
    modified_chars = char_list[:]
    for i in selected_indices:
        modified_chars[closing_indices[i][0]] = ''
        modified_chars[closing_indices[i][1]] = ''

    # Add the modified character list to the set of valid combinations
    valid_combinations.add(''.join(modified_chars))

# Print the valid combinations in lexicographical order
for combination in sorted(valid_combinations):
    print(combination)
