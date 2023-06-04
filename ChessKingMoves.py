def count_king_moves(x, y):
    moves = 0

    # Check left
    if x > 1:
        moves += 1

    # Check right
    if x < 8:
        moves += 1

    # Check up
    if y < 8:
        moves += 1

    # Check down
    if y > 1:
        moves += 1

    # Check diagonals
    if x > 1 and y < 8:
        moves += 1
    if x < 8 and y < 8:
        moves += 1
    if x > 1 and y > 1:
        moves += 1
    if x < 8 and y > 1:
        moves += 1

    return moves

# Get input coordinates
x = int(input("Enter the x-coordinate of the king: "))
y = int(input("Enter the y-coordinate of the king: "))

# Calculate and print the number of moves
num_moves = count_king_moves(x, y)
print("The king can make", num_moves, "moves.")
