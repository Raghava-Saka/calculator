logo = r''' _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a/b
def power(a,b):
    return a ** b
def calculator():
    a = float(input("What's the first no.?: "))

    accumulation = True
    while accumulation:
        operation_symbol = input('''
        +
        -
        *
        /
        ^ (power)
        Pick an operation:
        ''')

        b = float(input("What's the next no.?: "))

        operations = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide,
            "^" : power,
        }

        for symbol in operations:
            print(symbol)

        answer = operations[operation_symbol](a,b)
        print(f"{a} {operation_symbol} {b} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start with new calculations.")

        if choice == 'y':
            a = answer
        else:
            accumulation == False
            print("\n" * 20)
            print(logo)
            calculator()
calculator()