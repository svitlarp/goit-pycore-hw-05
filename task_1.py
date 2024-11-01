
def caching_fibonacci():
    '''Function to find corresponding number from fibonacci sequence 
    that use closure to store already founded values in a dictionary'''

    # Create a dictionary to store each number as a key, with its corresponding Fibonacci sequence value as the associated value.
    cache = dict()

    def fibonacci(n: int) -> int: 
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n] 
          
        # Recursive call  
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    return fibonacci    

fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

# n = 0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
# xn =0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	

# TestCase1 fibo from 0 (should return o)
assert fib(-3) == 0, "Test case 1 failed"

# TestCase2 fibo from 1 (should return 1)
assert fib(1) == 1, "Test case 2 failed"

# TestCase3 fibo from 11 (should return 89)
assert fib(11) == 89, "Test case 3 failed"

# TestCase4 fibo from 8 that takes fibo(8) from cache (should return 21)
assert fib(8) == 21, "Test case 4 failed"



