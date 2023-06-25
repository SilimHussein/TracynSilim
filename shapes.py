def guess_shape(num_sides):
    if num_sides == 3:
        return "Triangle"
    elif num_sides == 4:
        return "Quadrilateral"
    elif num_sides == 5:
        return "Pentagon"
    elif num_sides == 6:
        return "Hexagon"
    elif num_sides == 7:
        return "Heptagon"
    else:
        return "Unknown shape"

# Get the number of sides from the user
num_sides = int(input("Enter the number of sides (between 3 and 7): "))

# Guess the shape based on the number of sides
shape = guess_shape(num_sides)

# Print the guessed shape
print("The shape could be a", shape)
