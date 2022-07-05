## To run the tests in this file:
##      pip install pytest
##      pytest

from FizzBuzz import printFizzBuzz

def test_3_multiple():
    assert printFizzBuzz(3) == "Fizz"
    assert printFizzBuzz(6) == "Fizz"

def test_5_multiple():
    assert printFizzBuzz(5) == "Buzz"
    assert printFizzBuzz(10) == "Buzz"
    
def test_3_and_5_multiple():
    assert printFizzBuzz(15) == "FizzBuzz"
    assert printFizzBuzz(30) == "FizzBuzz"
    
def test_7_multiple():
    assert printFizzBuzz(7) == "Bang"
    assert printFizzBuzz(21) == "FizzBang"
    assert printFizzBuzz(105) == "FizzBuzzBang"
    
def test_11_multiple():
    assert printFizzBuzz(11) == "Bong"
    assert printFizzBuzz(22) == "Bong"
    assert printFizzBuzz(33) == "Bong"
    assert printFizzBuzz(44) == "Bong"
    assert printFizzBuzz(55) == "Bong"
    
def test_13_multiple():
    assert printFizzBuzz(65) == "FezzBuzz"
    assert printFizzBuzz(195) == "FizzFezzBuzz"
    assert printFizzBuzz(143) == "FezzBong"

def test_17_multiple():
    assert printFizzBuzz(255) == "BuzzFizz"
    
def test_prime_numbers():
    assert int(printFizzBuzz(19)) == 19
    assert int(printFizzBuzz(23))== 23
    assert int(printFizzBuzz(89)) == 89
    assert int(printFizzBuzz(97)) == 97
