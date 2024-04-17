def fib(n):

  if n == 0 or n == 1:
    return n
  memo = [0] * (n + 1)
  memo[0] = 0
  memo[1] = 1
  for i in range(2, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]
  return memo[n]

num_terms = int(input("Enter the number of terms: "))

print("Fibonacci Sequence: ")
for i in range(num_terms):
  print(fib(i), end=" ")

