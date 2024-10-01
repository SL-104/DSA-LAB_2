# Class TR
class TR():
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen the Right Triangle Maker-".center(self.width))
        print("-**********-\n".center(self.width))
        # Run the main program
        self.main()
        
    def main(self):
        while True:
            try:
                # Input height of the triangle
                n = int(input("Enter the height of the triangle: "))
                self.right(n) 

                # Run again
                self.again()
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
                self.main() 
                return
            # End the program, will not make again
            elif again == "no":
                print("Thank you! Goodbye!")
                return
            else:
                # If the input is not a "Yes" or a "No" it will raise an Invalid input and will loop until the required input is inputted
                print("Invalid input. Please try again.")


# Run the class TR
TR()

# Sample Output
## -You have chosen the Right Triangle Maker-
## -**********-
## Enter the height of the triangle: 6
## ******
## *****
## ****
## ***
## **
## *
##
## Would you like to calculate powers again? (Yes/No): No
## Thank you! Goodbye!