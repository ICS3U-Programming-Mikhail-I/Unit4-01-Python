# Copyright 2025 Mikhail Ibrahim
# Date: Apr 9, 2025
# Description: A crash-proof Python program that adds up numbers from 1 to user's input,
# only if it's a positive whole number.


def main():
    print("Welcome! This program adds numbers from 1 to the number you enter.")

    while True:
        user_input = input("Enter a positive whole number: ")

        if not user_input.isdigit():
            print("Error: Please enter digits only (no letters, symbols, or decimals).")
            continue  # Try again

        number = int(user_input)

        if number <= 0:
            print("Error: Number must be greater than 0.")
            continue  # Try again

        # Valid input - do the sum
        total = 0
        counter = 1

        while counter <= number:
            print(f"{counter} time(s) through the loop.")
            total += counter
            counter += 1

        print(f"The sum of numbers from 1 to {number} is {total}.")
        break  # Exit the loop after success


# Run the program
if __name__ == "__main__":
    main()
