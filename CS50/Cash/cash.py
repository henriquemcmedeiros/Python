# Include libraries
from cs50 import get_float

def main():
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while True:
        cents = get_float("Change owed: ")
        if cents > 0:
            break

    # Calculate cents
    while cents >= 0.25:
        cents -= 0.25
        quarters += 1

    while cents >= 0.10:
        cents -= 0.10
        dimes += 1

    while cents >= 0.05:
        cents -= 0.05
        nickels += 1

    while cents >= 0.01:
        cents -= 0.01
        pennies += 1

    total = quarters + dimes + nickels + pennies
    print(total)

# Run the main function
main()