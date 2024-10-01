# Class Array
class Array():
        
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-Cube of Integers-".center(self.width))
        print("-Compute for the cube of integers per element-\n".center(self.width))
        # Run the main program
        self.main()


    def main(self):
        elements = self.ar_inp()
        self.cubes(elements)

        # Run again
        self.again()

    def ar_inp(self):
        while True:
            try:
                # Step 1: Input the size of the array
                size = int(input("Enter the size of the array: "))
                if size <= 0:
                    print("Size must be a positive integer. Please try again.")
                    continue
                
                # Input the elements of the array
                elements = list(map(int, input(f"Enter {size} elements separated by space: ").split()))

                # Check if the number of elements matches the specified size of the array
                if len(elements) != size:
                    print(f"Invalid input. Expected {size} elements, but got {len(elements)}. Please input again.")
                    continue
                
                return elements  # Return the valid elements list
            
            # If the input is not a number it will raise an Invalid input and will loop until the required input is inputted   
            except ValueError:
                print("Invalid input. Please enter a number.\n")

    def cubes(self, elements):
        # The cube of each element
        for cu in elements:
            print(cu ** 3)


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


# Run the class Array
Array()


# Sample Output
## -Cube of Integers-
## -Compute for the cube of integers per element-
## Enter the size of the array: 4
## Enter 4 elements separated by space: 1 2 3 4
## 1 
## Would you like to calculate powers again? (Yes/No): No
## Thank you! Goodbye!

