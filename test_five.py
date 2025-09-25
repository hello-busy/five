#!/usr/bin/env python3
"""
Tests for the five module
"""

import five

def test_is_five():
    """Test the is_five function"""
    assert five.is_five(5) == True
    assert five.is_five(4) == False
    assert five.is_five(6) == False
    assert five.is_five(0) == False
    print("✓ is_five tests passed")

def test_powers_of_five():
    """Test the powers_of_five function"""
    result = five.powers_of_five(3)
    expected = [1, 5, 25, 125]
    assert result == expected
    print("✓ powers_of_five tests passed")

def test_factors_of_five():
    """Test the factors_of_five function"""
    result = five.factors_of_five()
    expected = [1, 5]
    assert result == expected
    print("✓ factors_of_five tests passed")

def test_multiples_of_five():
    """Test the multiples_of_five function"""
    result = five.multiples_of_five(5)
    expected = [5, 10, 15, 20, 25]
    assert result == expected
    print("✓ multiples_of_five tests passed")

def test_fibonacci_five():
    """Test the fibonacci_five function"""
    result = five.fibonacci_five()
    expected = [0, 1, 1, 2, 3]
    assert result == expected
    print("✓ fibonacci_five tests passed")

def test_count_to_five():
    """Test the count_to_five function"""
    result = five.count_to_five()
    expected = [1, 2, 3, 4, 5]
    assert result == expected
    print("✓ count_to_five tests passed")

def test_five_facts():
    """Test the five_facts function"""
    result = five.five_facts()
    assert len(result) == 5
    assert all(isinstance(fact, str) for fact in result)
    print("✓ five_facts tests passed")

def main():
    """Run all tests"""
    print("Running tests for five module...")
    print()
    
    test_is_five()
    test_powers_of_five()
    test_factors_of_five()
    test_multiples_of_five()
    test_fibonacci_five()
    test_count_to_five()
    test_five_facts()
    
    print()
    print("All tests passed! ✨")

if __name__ == "__main__":
    main()