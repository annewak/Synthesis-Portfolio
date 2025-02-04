def show_results(num1, num2, results):
    operations = ["sum", "difference", "product", "quotient"]
    for operation, result in zip(operations, results):
        print(f"The {operation} of {num1} and {num2} is {result}")
    save_results(num1, num2, results)

def save_results(num1, num2, results):
    operations = ["sum", "difference", "product", "quotient"]
    with open("calculations.txt", "a") as file:
        for operation, result in zip(operations, results):
            file.write(f"The {operation} of {num1} and {num2} is {result}\n")
    
