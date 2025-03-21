import sys

if len(sys.argv) != 3:
    print("Usage: python calculator.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except ValueError:
    print("Please provide two valid numbers.")
    sys.exit(1)

result = num1 * num2
print(f"{result}")