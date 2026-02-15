class User:
    # to get the row/col numbers
    @staticmethod
    def get_input(num, min=None, max=None):
        while True:
            try:
                value = int(input(num))
                # keeps user input within the designated range
                if min is not None and value < min:
                    print(f"Please enter a number greater than or equal to {min}.")
                elif max is not None and value > max:
                    print(f"Please enter a number less than or equal to {max}.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                
    # to get bomb probability
    @staticmethod
    def get_float_input(num, min=0.0, max=1.0):
        while True:
            try:
                value = float(input(num))
                # keeps user input within the designated range
                if value < min or value > max:
                    print(f"Please enter a number between {min} and {max}.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid decimal number.")
