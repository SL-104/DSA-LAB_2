# ------------------------------------------- #
#   Name: Sophia Queen Lim                    #
#   Course, Year, and Section: BSCPE 2-3      #
#   Professor: Engr. Godofredo Avena          #
#   Subject: Data Structure and Algorithm     #
#   Lab Activity 2                            #
# ------------------------------------------- #

# Picking an Exercise:
class Pick:
    def __init__(self):
        self.run()

    def run(self):
        # Loop until an exercise is selected
        while True:
            try:
                # Choosing an exercise
                choice = int(input("\nPlease pick an exercise to run\n"
                                   "Exercise 1: Class Rivera\n"
                                   "Exercise 2: Cube of Integers\n"
                                   "Exercise 3: Hollow Square Maker\n"
                                   "Exercise 4: Right Triangle Maker\n"
                                   "(1, 2, 3, or 4): "))
                # Select an exercise and run its respective class
                if choice == 1:
                    self.run_exercise(Rivera)
                elif choice == 2:
                    self.run_exercise(Array)
                elif choice == 3:
                    self.run_exercise(Hollow)
                elif choice == 4:
                    self.run_exercise(TR)
                else:
                    print("Invalid choice. Please choose again.\n")
            
            # If the input is not a number it will raise an Invalid input and will loop until correct input is given
            except ValueError:
                print("Please enter a valid integer.\n")

    def run_exercise(self, exercise_class):
        # Run the selected exercise
        exercise = exercise_class()
        while True:
            if not exercise.run():  # If the exercise ends and returns False
                print("Thank You! Goodbye!")
                exit()


# Class Rivera
class Rivera:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen to help the class of Mrs. Rivera-".center(self.width))
        print("-Recursive method to calculate powers-\n".center(self.width))

    def run(self):
        # Start the main part of the exercise
        self.main()
        # Return the result of the again() method
        return self.again()

    def main(self):
        while True:
            try:
                # Input the base and the exponent numbers
                base = int(input("Please input a base number: "))
                exp = int(input("Please input an exponent number: "))

                # Calculate the power using recursion
                result = self.powpow(base, exp)

                # Print the result
                print(f"{base}^{exp} = {result}")
                break

            # If the input is not a number it will raise an Invalid input and will loop until the required input is inputted   
            except ValueError:
                print("Invalid input. Please enter a number.\n")

    def powpow(self, base, exp):
        # Any number raised to the power of 0 is 1
        if exp == 0:
            return 1
        
        # Handle negative exponents
        elif exp < 0:
            return 1 / self.powpow(base, -exp)
        else:
            # Multiply the base by the result of base raised to (exponent - 1)
            return base * self.powpow(base, exp - 1)
    
    # Asking the user if they want to calculate again
    def again(self):
        while True:
            again = input("\nWould you like to calculate powers again? (Yes/No): ").strip().lower()
            # Will make again
            if again == "yes":
                return True  
            # End the program, will not make again
            elif again == "no":
                return self.pick_another_program()
            else:
                # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
                print("Invalid input. Please try again.")

    # Picking another program from the Pick class
    def pick_another_program(self):
        while True:
            pick_another = input("\nWould you like to pick another program? (Yes/No): ").strip().lower()
            # Will pick again
            if pick_another == "yes":
                Pick()
            # End the program, will not pick again
            elif pick_another == "no":
                return False
            # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
            else:
                print("Invalid input. Please try again.")


# Class Array
class Array:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-Cube of Integers-".center(self.width))
        print("-Compute for the cube of integers per element-\n".center(self.width))

    def run(self):
        # Start the main part of the exercise
        self.main()
        return self.again()

    def main(self):
        elements = self.ar_inp()
        self.cubes(elements)

    def ar_inp(self):
        while True:
            try:
                # Input the size of the array
                size = int(input("Enter the size of the array: "))
                if size <= 0:
                    print("Size must be a positive integer. Please try again.")
                    continue
                
                # Input the elements of the array
                elements = list(map(int, input(f"Enter the elements separated by space: ").split()))

                # Check if the number of elements matches the specified size of the array
                if len(elements) != size:
                    print(f"Invalid input. Expected {size} elements, but got {len(elements)}. Please input again.")
                    continue
                
                return elements  # Return the valid elements list
            
            # If the input is not a number it will raise an Invalid input and will loop until correct input is given
            except ValueError:
                print("Invalid input. Please enter a number.\n")

    def cubes(self, elements):
        # The cube of each element
        for cu in elements:
            print(cu ** 3)

    # Asking the user if they want to calculate again
    def again(self):
        while True:
            again = input("\nWould you like to calculate again? (Yes/No): ").strip().lower()
            # Will calculate again
            if again == "yes":
                return True 
            # End the program, will not calculate again
            elif again == "no":
                return self.pick_another_program()
            # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
            else:
                print("Invalid input. Please try again.")

    # Picking another program from the Pick class
    def pick_another_program(self):
        while True:
            pick_another = input("\nWould you like to pick another program? (Yes/No): ").strip().lower()
            # Will pick again
            if pick_another == "yes":
                Pick()
            # End the program, will not pick again
            elif pick_another == "no":
                return False
            # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
            else:
                print("Invalid input. Please try again.")


# Class Hollow
class Hollow:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen the Hollow Square Maker-".center(self.width))
        print("-**********-\n".center(self.width))

    def run(self):
        # Start the main part of the exercise
        self.main()
        return self.again()

    def main(self):
        while True:
            try:
                # Input the side length of the square
                n = int(input("Enter the side length of the square: "))
                self.row(n)
                break

            # If the input is not a number it will raise an Invalid input and will loop until the required input is inputted               
            except ValueError:
                print("Invalid input. Please enter a number.\n")

    def row(self, n):
        # First row filled x
        f_row = 'x' * n
        # Last row filled x
        l_row = 'x' * n
        # Middle row with spaces in between
        mid_row = 'x' + ' ' * (n - 2) + 'x'

        # Print the first row
        print(f_row)
        # Print the middle rows
        for i in range(n - 2):
            print(mid_row)
        # Print the last row
        print(l_row)

    # Asking the user if they want to make again
    def again(self):
        while True:
            again = input("\nWould you like to create again? (Yes/No): ").strip().lower()
            # Will make again
            if again == "yes":
                return True  
            # End the program, will not make again
            elif again == "no":
                return self.pick_another_program()
            else:
                print("Invalid input. Please try again.")

    # Picking another program from the Pick class
    def pick_another_program(self):
        while True:
            pick_another = input("\nWould you like to pick another program? (Yes/No): ").strip().lower()
            # Will pick again
            if pick_another == "yes":
                Pick()
            # End the program, will not pick again
            elif pick_another == "no":
                return False
            # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
            else:
                print("Invalid input. Please try again.")


# Class TR
class TR:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen the Inverted Right Triangle Maker-".center(self.width))
        print("-**********-\n".center(self.width))

    def run(self):
        # Start the main part of the exercise
        self.main()
        return self.again()

    def main(self):
        while True:
            try:
                # Input height of the triangle
                n = int(input("Enter the height of the triangle: "))
                self.right(n)
                break

            # If the input is not a number it will raise an Invalid input and will loop until the required input is inputted               
            except ValueError:
                print("Invalid input. Please enter a number.\n")
    
    # Making of the right triangle *
    def right(self, n):
        for i in range(n, 0, -1):
            print("*" * i)

    # Asking the user if they want to make again
    def again(self):
        while True:
            again = input("\nWould you like to create again? (Yes/No): ").strip().lower()
            # Will make again
            if again == "yes":
                return True  
            # End the program, will not make again
            elif again == "no":
                return self.pick_another_program() 
            # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
            else:
                print("Invalid input. Please try again.")
    
    # Picking another program from the Pick class
    def pick_another_program(self):
        while True:
            pick_another = input("\nWould you like to pick another program? (Yes/No): ").strip().lower()
            # Will pick again
            if pick_another == "yes":
                Pick()
            # End the program, will not pick again
            elif pick_another == "no":
                return False
            # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
            else:
                print("Invalid input. Please try again.")


# Run the Program
Pick()




# Sample Output

# Please pick an exercise to run
# "Exercise 1: Class Rivera
# Exercise 2: Cube of Integers
# Exercise 3: Hollow Square Maker
# Exercise 4: Right Triangle Maker
# (1, 2, 3, or 4): 1

## -You have chosen to help the class of Mrs. Rivera-
## -Recursive method to calculate powers-
##
## Please input a base number: 5
## Please input an exponent number: 3
## 5^3 = 125
##
## Would you like to calculate powers again? (Yes/No): No
##
## Would you like to pick another program? (Yes/No): Yes

# Please pick an exercise to run
# "Exercise 1: Class Rivera
# Exercise 2: Cube of Integers
# Exercise 3: Hollow Square Maker
# Exercise 4: Right Triangle Maker
# (1, 2, 3, or 4): 2

## -Cube of Integers-
## -Compute for the cube of integers per element-
##
## Enter the size of the array: 4
## Enter the elements separated by space: 1 2 3 4
## 1 
## 8
## 27
## 64
##
## Would you like to calculate again? (Yes/No): No
## Would you like to pick another program? (Yes/No): Yes

# Please pick an exercise to run
# "Exercise 1: Class Rivera
# Exercise 2: Cube of Integers
# Exercise 3: Hollow Square Maker
# Exercise 4: Right Triangle Maker
# (1, 2, 3, or 4): 3

## -You have chosen the Hollow Square Maker-
## -**********-
##
## Enter the side length of the square: 5
## *****
## *   *
## *   * 
## *   *
## *****
##
## Would you like to create again? (Yes/No): No
## Would you like to pick another program? (Yes/No): Yes

# Please pick an exercise to run
# "Exercise 1: Class Rivera
# Exercise 2: Cube of Integers
# Exercise 3: Hollow Square Maker
# Exercise 4: Inverted Right Triangle Maker
# (1, 2, 3, or 4): 4

## -You have chosen the Inverted Right Triangle Maker-
## -**********-
##
## Enter the height of the triangle: 6
## ******
## *****
## ****
## ***
## **
## *
##
## Would you like to create again? (Yes/No): No
## Would you like to pick another program? (Yes/No): No
## Thank you! Goodbye!
