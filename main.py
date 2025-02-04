from modules.input import enter_numbers
from modules.processing import add, subtract, multiply, divide
from modules.output import show_results

def main():
    num1, num2 = enter_numbers()
    results = [add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2)]
    show_results(num1, num2, results)

if __name__ == "__main__":
    main()
