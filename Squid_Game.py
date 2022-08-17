group = int(input("How many groups are there? "))#Asking the user the amount of the groups.

if group <= 0:
    print("Invalid input") #If the group input is invalid the code won't execute anymore.

else:

    for i in range(1, group + 1, 1):  #This for loop is for groups.
        players = int(input("How many players are there at the group?")) #We defined a varieble which would ask the user for an input if all the previous conditions were true.

        if players <= 0:
            print("Invalid input") #If the player input is invalid the code won't execute anymore.
        else:

            for j in range(1, players + 1, 1):
                print("*Group", i, "-Player", j, "*") #If all the previous conditions are true it will display the players turn starting from group one player one
                shape = int(input("Select a shape (1= Square, 2= Triangle, 3= Equilateral triangle, 4= Sandglass):"))#We asked user to pick a shape.

                if shape <= 0 or shape > 4: # Shapes should be between 1 and 4 so we wrote a if statement.
                    players -= 1 # If the shape value is invalid the player who typed that value will be eliminated.
                    print("Oops invalid choice! Player", j, "is eliminated!")

                if shape == 1:
                    print("Shape is a square!") #We asigned the numbers between 1 and 4 shapes 1
                    size = int(input("Select the size of the shape (2/3/4/5/6): "))

                    if size <= 1 or size > 6:# If the size value is invalid the player who typed that value will be eliminated.
                        players -= 1
                        print("Oops invalid choice! Player", j, "is eliminated!")

                    else:
                        guess = int(input("How many stars exist in this square? "))
                        for c in range(size):

                            for y in range(size):
                                print("*", end=" ")

                            print()

                        if guess == size ** 2:
                            print("Total number of stars:", size ** 2, ", Congratulations! Player", j, "wins the game!")

                        if guess != size ** 2:
                            players -= 1
                            print("Total number of stars:", size ** 2, ", Oops, Player", j, "is eliminated!")
                            print()

                if shape == 2:
                    print("Shape is a triangle!")
                    size = int(input("Select the size of the shape (2/3/4/5/6): "))

                    if size <= 1 or size > 6:
                        players -= 1
                        print("Oops invalid choice! Player", j, "is eliminated!")

                    else:
                        guess = int(input("How many stars exist in this triangle? "))
                        for k in range(1, size + 1):
                            for l in range(1, (size - k) + 1):  # for loop to display spaces in the shape.
                                print(" ", end=" ")

                            for l in range(1, k + 1):  # for loop to display * in the shape.
                                print("*", end=" ")

                            print()
                        if guess == (size * (size + 1)) / 2:
                            print("Total number of stars:", int((size * (size + 1)) / 2), ", Congratulations! Player", j,
                                  "wins the game!")

                        if guess != (size * (size + 1)) / 2:
                            players -= 1
                            print("Total number of stars:", int((size * (size + 1)) / 2), ", Oops, Player", j,
                                  "is eliminated!")
                            print()

                if shape == 3:
                    print("Shape is a equilateral triangle!")
                    size = int(input("Select the size of the shape (2/3/4/5/6): "))

                    if size <= 1 or size > 6:
                        players -= 1
                        print("Oops invalid choice! Player", j, "is eliminated!")

                    else:
                        guess = int(input("How many stars exist in this triangle?"))
                        for o in range(size, 0, -1):
                            for m in range(size - o):
                                print(" ", end=" ")  # printing space and staying in same line

                            for m in range(2 * o - 1):
                                print("*", end=" ")  # printing * and staying in same line
                            print()  # printing new line

                        if guess == size ** 2:
                            print("Total number of stars:", size ** 2, ", Congratulations! Player", j, "wins the game!")

                        if guess != size ** 2:
                            players -= 1
                            print("Total number of stars:", size ** 2, ", Oops, Player", j, "is eliminated!")

                if shape == 4:
                    print("Shape is a sandglass!")
                    size = int(input("Select the size of the shape (size must be odd!): "))

                    if size <= 0 or size % 2 == 0:
                        players -= 1
                        print("Oops invalid choice! Player", j, "is eliminated!")
                    else:
                        guess = int(input("How many stars exist in this sandglass? "))

                        size = int((size + 2) / 2)
                        # Upper part
                        for p in range(size, 0, -1):
                            for u in range(size - p):
                                print(" ", end=" ")
                            for u in range(1, 2 * p):
                                print("*", end=" ")
                            print()

                        # Lower part
                        for p in range(2, size + 1):
                            for u in range(size - p):
                                print(" ", end=" ")
                            for u in range(1, 2 * p):
                                print("*", end=" ")
                            print()

                        if guess == ((size ** 2) * 2) - 1:
                            print("Total number of stars:", int(((size ** 2) * 2) - 1), " Player", j, " wins the game!")

                        if guess != ((size ** 2) * 2) - 1:
                            players -= 1
                            print("Total number of stars:", int(((size ** 2) * 2) - 1), " Player", j, " is eliminated!")

            print(players, "player(s) stayed alive in Group", i, "!")
print("----End of the game----")
