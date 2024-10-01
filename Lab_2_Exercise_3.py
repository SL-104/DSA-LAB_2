# Class Hollow
class Hollow():
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen the Hollow Square Maker-".center(self.width))
        print("-**********-\n".center(self.width))
        # Run the main program
        self.main()

    def main(self):
        while True:
            try:
                # Input the side length of the square
                n = int(input("Enter the side length of the square: "))
                self.row(n)
                # Run again
                self.again()
                break

            # If the input is not a number it will raise an Invalid input and will loop until the required input is inputted               
            except ValueError:
                print("Invalid input. Please enter a number.\n")


    def row(self, n):
        # First row filled x
        f_row = 'x' * n
        # Last row filled x
        l_row  = 'x' * n
        # Middle row with spaces inbetween
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
                self.main() 
                return
            # End the program, will not make again
            elif again == "no":
                print("Thank you! Goodbye!")
                return
            else:
                # If the input is not a "Yes" or a "No" it will raise an Invalid input and will loop until the required input is inputted
                print("Invalid input. Please try again.")

# Run the class Hollow
Hollow()


# Sample Output
## -You have chosen the Hollow Square Maker-
## -**********-
## Enter the side length of the square: 5
## *****
## *   *
## *   * 
## *   *
## *****
##
## Would you like to calculate powers again? (Yes/No): No
## Thank you! Goodbye!