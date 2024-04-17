def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence
print("Fibonacci Sequence: ")
for i in range(1, num_terms + 1):
  print(fibonacci(i), end=" ")
