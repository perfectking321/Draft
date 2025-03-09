def swap_numbers():
    """Swaps two numbers entered by the user."""

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print(f"Original numbers: num1 = {num1}, num2 = {num2}")

    # Swapping using a temporary variable
    temp = num1
    num1 = num2
    num2 = temp

    print(f"Swapped numbers: num1 = {num1}, num2 = {num2}")

if __name__ == "__main__":
    swap_numbers()
