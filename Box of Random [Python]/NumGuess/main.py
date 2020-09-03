import random
#import traceback

# Generate the number
int_num = random.randrange(1, 101)
int_attempts = 7

print("A random number be tween 1 and 100 has been generated.")

# Start the guessing loop
while int_attempts != 0:
    print("Enter your input:")

    try:
        # Grab input
        int_input = int(input())

        # Check if too low or too high
        if int_input < int_num:
            print("Too low! Try again.")
            int_attempts -= 1
            print("Attempts remaining: " + str(int_attempts))
            print() # Blank line

        elif int_input > int_num:
            print("Too high! Try again.")
            int_attempts -= 1
            print("Attempts remaining: " + str(int_attempts))
            print() # Blank line

        # If neither, then answer is correct
        else:
            print("Correct!")
            int_attempts = 0
            
    # Catch anything other than a number
    except Exception as e:
        print("Error: {}".format(type(e).__name__))
        print("Only numbers are allowed.")
