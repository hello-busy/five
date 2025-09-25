#!/usr/bin/env python3
"""
Five - A simple Python module demonstrating operations with the number 5
"""

def is_five(number):
    """Check if a number is exactly 5"""
    return number == 5

def powers_of_five(max_power=5):
    """Generate first n powers of 5"""
    return [5 ** i for i in range(max_power + 1)]

def factors_of_five():
    """Return the factors of 5"""
    return [1, 5]

def multiples_of_five(count=10):
    """Generate first n multiples of 5"""
    return [5 * i for i in range(1, count + 1)]

def fibonacci_five():
    """Return the first 5 numbers in the Fibonacci sequence"""
    fib = [0, 1]
    for i in range(3):
        fib.append(fib[-1] + fib[-2])
    return fib

def count_to_five():
    """Count from 1 to 5"""
    return list(range(1, 6))

def five_facts():
    """Return interesting facts about the number 5"""
    return [
        "5 is the 3rd prime number",
        "5 is the number of fingers on a human hand",
        "5 is the number of senses humans have",
        "A pentagon has 5 sides",
        "5 is the atomic number of boron"
    ]

def main():
    """Main function to demonstrate all five-related operations"""
    print("=== Welcome to Five! ===")
    print()
    
    print("Is 5 equal to 5?", is_five(5))
    print("Is 4 equal to 5?", is_five(4))
    print()
    
    print("Powers of 5:", powers_of_five())
    print("Factors of 5:", factors_of_five())
    print("First 10 multiples of 5:", multiples_of_five())
    print()
    
    print("First 5 Fibonacci numbers:", fibonacci_five())
    print("Count to 5:", count_to_five())
    print()
    
    print("Five Facts:")
    for i, fact in enumerate(five_facts(), 1):
        print(f"{i}. {fact}")

if __name__ == "__main__":
    main()