#Name : Reshma Sri Murakonda
#Student ID : 101282055

#Importing SYS
import sys
x = (sys.argv[1])
c = int(sys.argv[1])

# Asking user to input an integer assuming that the user will put a positive integer.
print("Please enter a value: ")
I = int(input())

# Multiplying the inputted integer to 7.
I = I * 7
print("The result multiplied by 7 gives: ",I)

# Adding the result to the value entered in the Command prompt.
I = c + I
print("The result added to the command prompt gives: ",I)

# Adding the resulted value to the integer that is one more than itself.
I = I+(I+1)
print("The result added to a number greater than itself gives: ",I)

# Dividing the resulted value with 6.
I = I%6
print("The result divided by 6 leaves the remainder: ",I)

# Multiplying the result with 28.333433
I = I*28.333433
print("The value multiplied by 28.333433 gives: ",I)

# Convert it to an integer
I = int(I)
print("After converting to an integer, the new value is: ",I)

# Convert it to a character
I = chr(I)
print("After converting to a character, the result is: ",I)

# Printing the Final Result in triangle brackets
print("The final result is: <",I,">")