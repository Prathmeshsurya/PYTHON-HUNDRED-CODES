# Function to calculate GCD using the Euclidean algorithm
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD using the custom function
gcd = calculate_gcd(num1, num2)

# Print the GCD
print(f"The GCD of {num1} and {num2} is: {gcd}")
