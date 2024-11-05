def minimum_scalar_product(test_cases):
    results = []
    for case_number, (n, v1, v2) in enumerate(test_cases, start=1):
        # Sort v1 in ascending order and v2 in descending order
        v1.sort()
        v2.sort(reverse=True)
        
        # Calculate the minimum scalar product
        min_scalar_product = sum(x * y for x, y in zip(v1, v2))
        
        # Store the result with the required format
        results.append(f"Case #{case_number}: {min_scalar_product}")
    
    return results

T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    test_cases.append((n, v1, v2))

results = minimum_scalar_product(test_cases)
print("\n".join(results))
