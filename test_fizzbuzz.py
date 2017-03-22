from fizzbuzz import fizzbuzz
import pytest

def test_fizzbuzz_1():
	assert fizzbuzz(1) == 1
	
def test_fizzbuzz_3():
	assert fizzbuzz(3) == 'fizz'
	
def test_fizzbuzz_50():
	assert fizzbuzz(50) == 'buzz'
	
def test_fizzbuzz_150():
	assert fizzbuzz(150) == 'fizzbuzz'