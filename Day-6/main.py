version = "0.1.0"
status = "Development"

def get_integer(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number, for example 7 or -3.")


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a number, for example 4 or -2.5.")
            continue
        if not math.isfinite(value):
            print("That value is not a usable number. Try again.")
            continue
        return value


def divide_numbers(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return first_number / second_number


def safe_division():
    first = get_number("First number: ")
    second = get_number("Second number: ")
    try:
        result = divide_numbers(first, second)
    except ZeroDivisionError as error:
        print(f"Error: {error} Choose a non-zero second number.")
    else:
        print(f"{first} / {second} = {result}")
    finally:
        print("Division attempt finished.")


ERROR_EXAMPLES = [
    ("if age > 18\n    print('adult')",
     "Syntax error: missing colon after the if condition, so Python "
     "cannot parse the code and the program never starts."),
    ("numbers = [4, 8, 12]\nprint(numbers[3])",
     "Exception (IndexError): the code is valid and starts running, but "
     "index 3 does not exist in a 3-item list (valid indexes are 0-2)."),
    ("scores = [80, 90, 100]\naverage = sum(scores) / 2",
     "Logic error: it runs without any error but divides by 2 instead of "
     "len(scores), so the answer (135.0) is wrong."),
]


def show_error_examples():
    for number, (code, explanation) in enumerate(ERROR_EXAMPLES, start=1):
        print(f"\nExample {number}:\n{code}\n-> {explanation}")


def intentional_value_error():
    quantity = int("five")
    return quantity


def fixed_value_error():
    text = "five"
    try:
        return int(text)
    except ValueError:
        print(f"'{text}' is not a whole number; using 5 as a default.")
        return 5


def demo_specific_exceptions():
    try:
        int("abc")
    except ValueError:
        print("ValueError caught: 'abc' cannot be converted to an integer.")

    try:
        10 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError caught: cannot divide by zero.")


def main():
    while True:
        print("\n1) Safe integer  2) Safe division  3) Error examples")
        print("4) Specific exceptions  5) Fixed ValueError  6) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            print("You entered:", get_integer("Enter an integer: "))
        elif choice == "2":
            safe_division()
        elif choice == "3":
            show_error_examples()
        elif choice == "4":
            demo_specific_exceptions()
        elif choice == "5":
            print("Result:", fixed_value_error())
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()