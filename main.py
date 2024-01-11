from art import logo
from calc import add, subtract, multiply, divide

OPERATIONS = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calculate():
    num1 = float(input("What's the first number?: "))
    should_continue = True
    while should_continue:
        for op in OPERATIONS:
            print(op)
        user_operation = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        function = OPERATIONS[user_operation]
        ans = function(num1, num2)
        print(f"{num1} {user_operation} {num2} = {ans}")
        response = input(
            f'Type "yes" if you want to do another calculation with {ans}, otherwise type "no" to start a new calculation or "exit" to close the program: ').lower()
        if response == "yes":
            num1 = ans
        elif response == "no":
            calculate()
            should_continue = False
        else:
            print("Bye!")
            should_continue = False


if __name__ == '__main__':
    print(logo)
    calculate()
