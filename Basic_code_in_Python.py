# Basic operations and loop examples in Python

# Function for basic arithmetic operations
def arithmetic_operations(a, b):
    print(f"Addition of {a} and {b}: {a + b}")
    print(f"Subtraction of {b} from {a}: {a - b}")
    print(f"Multiplication of {a} and {b}: {a * b}")
    print(f"Division of {a} by {b}: {a / b}")

# Function to demonstrate for loop with a range
def for_loop_range(n):
    print(f"For loop with range 1 to {n}:")
    for i in range(1,n + 1):
        print(i, end=' ')
    print()

# Function to demonstrate while loop
def while_loop(n):
    print(f"While loop with range 1 to {n}:")
    i = 1
    while i <= n:
        print(i, end=' ')
        i += 1
    print()

# Function to demonstrate for loop with a list
def for_loop_list(lst):
    print("For loop with list:")
    for item in lst:
        print(item, end=' ')
    print()

# Function to demonstrate nested loops
def nested_loops(n):
    print(f"Nested loops with range 1 to {n}:")
    for i in range(1,n + 1):
        for j in range(1,i + 1):
            print(j, end=' ')
        print()

# Function to demonstrate loop with conditionals
def loop_with_conditionals(n):
    print(f"Loop with conditionals up to {n}:")
    for i in range(1,n+1):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

# Main function to execute the script
def main():
    # Basic arithmetic operations
    a , b = 10 , 5

    arithmetic_operations(a, b)

    # For loop with range
    for_loop_range(5)

    # While loop
    while_loop(5)

    # For loop with a list
    sample_list = ['apple', 'banana', 'orange']
    for_loop_list(sample_list)

    # Nested loops
    nested_loops(5)

    # Loop with conditionals
    loop_with_conditionals(5)

# Run the main function
if __name__ == "__main__":
    main()
