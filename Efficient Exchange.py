#dictionary to store calculated values
memo = {0: 0, 1: 1}

#calculate the result for a given input
def calculate_result(n):
    # Check if the result is already memoized
    if n in memo:
        return memo[n]

    # Calculate the last digit of n
    last_digit = n % 10

    # Calculate the two possible results recursively
    result1 = last_digit + calculate_result(n // 10)
    result2 = 10 - last_digit + calculate_result((n // 10) + 1)

    # Store the minimum of the two results in the memo dictionary
    memo[n] = min(result1, result2)

    return memo[n]

# Get user input and calculate the result
user_input = int(input())
result = calculate_result(user_input)
print(result)
