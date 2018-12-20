# Find the square root of real and complex numbers.
# Import the complex math module.
Import cmath

# Create a vareable to store the number that shall be operated on.
num = input(float("Enter a number to find it's square root: "))

# Now to find the square root...
square_root = cmath.sqrt(num)

# Printing out the square root.
print ("The square root is %d." % (square_root))