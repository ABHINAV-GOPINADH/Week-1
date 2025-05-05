def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("Fibonacci sequence up to", n, "terms:")
    
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n_terms = int(input("Enter the number of terms: "))
fibonacci(n_terms)
