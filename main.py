# Calculuator
def calculate():
    """ Calculates operation """
    number_a =  int(float(input('Enter number:')))
    number_b =  int(float(input('Enter another number: ')))
    operation = str(input('Enter operation: ')).strip()
    if operation == "+":
        print(f'Sum:{number_a + number_b}') 
    elif operation == "-":
        print(f'Difference:{number_a - number_b}')
    elif operation == "*":
        print(f'Product:{number_a * number_b}')
    elif operation == "/":
        print(f'Quotient:{round(number_a / number_b, 2)}')
    else:
        print("invalid input")

    def again():
        """ Asks if user wants to use calculator again """ 
        answer = (input("Wanna use again? \nY for Yes, N for No: ").strip()).upper()
        if answer == "Y":
            calculate()
        elif answer == "N":
            print('Logging off.......')
        else:
            again()
    again()    

calculate()


    