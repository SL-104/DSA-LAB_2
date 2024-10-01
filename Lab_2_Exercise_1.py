# Class Rivera
class Rivera:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen to help the class of Mrs. Rivera-".center(self.width))
        print("-Recursive method to calculate powers-\n".center(self.width))
        # Run the main program
        self.main()

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
                
                # Run again
                self.again()
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
                self.main()
                return  
            # End the program, will not make again
            elif again == "no":
                print("Thank you! Goodbye!")
                return
            else:
                # If the input is not "Yes" or "No" it will raise an Invalid input and will loop until correct input is given
                print("Invalid input. Please try again.")

# Run the class Rivera
Rivera()
