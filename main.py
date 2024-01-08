from assets import logo

operators = ["+", "-", "*", "/"]
print(logo)
def calc():
    first_number = int(input("Give me the first number: "))
    for i in operators:
        print(i)
    
    continue_calc = True

    while continue_calc:

        operator = input("Pick the operator: ")
        second_number = int(input("Give me the second number: "))

        def add(first_number, second_number):
            result = first_number + second_number
            return result
        def subtract(first_number, second_number):
            result = first_number - second_number
            return result
        def divide(first_number, second_number):
            result = first_number / second_number
            return result
        def multiply(first_number, second_number):
            result = first_number * second_number
            return result
        
        if operator == "+":
            result =add(first_number, second_number)
        elif operator == "-":
            result=subtract(first_number, second_number)
        elif operator == "/":
            result=divide(first_number, second_number)
        elif operator == "*":
            result=multiply(first_number, second_number)

        print(f"Yot result is {result}\n")

        should_continue = input(f"type 'y' to continue calculating with {result}, 'n' to start new calculations or 'exit' to end: ")

        if should_continue == "y":
            first_number = result
        if should_continue == "n":
            print("\n"*50)
            continue_calc = False
            calc()
        if should_continue=="exit":
            continue_calc = False
            


calc()