# Get input dimensions
A = int(input("Enter length of the box: "))
B = int(input("Enter width of the box: "))
C = int(input("Enter height of the box: "))
X = int(input("Enter width of the doorway: "))
Y = int(input("Enter height of the doorway: "))

# Check if the box can be carried
if (A <= X and B <= Y) or (B <= X and A <= Y) or (A <= X and C <= Y) or (C <= X and A <= Y) or (B <= X and C <= Y) or (C <= X and B <= Y):
    print("The box can be carried")
else:
    print("The box cannot be carried")
