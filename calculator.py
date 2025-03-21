import sys



# function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# create main function
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python calculator.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(multiply(num1, num2))
    except ValueError:
        print("Please provide two valid numbers.")
        sys.exit(1)