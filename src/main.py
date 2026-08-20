from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    # Prompt user for a number
    user_input = input("Enter a number: ")
    n = float(user_input)

    sq = square(n)
    even_odd = "even" if is_even(n) else "odd"
    fahrenheit = celsius_to_fahrenheit(n)

    print(f"Square: {sq}")
    print(f"Parity: {even_odd}")
    print(f"Fahrenheit (if {n}°C): {fahrenheit}")

    # Greeting
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()
