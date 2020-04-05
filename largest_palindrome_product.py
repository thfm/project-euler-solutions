"""
Source: https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    digits = str(num)
    for i in range(int(len(digits) / 2)):
        if digits[i] != digits[-i - 1]:
            return False

    return True

palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product):
            palindromes.append(product)

print(max(palindromes))
